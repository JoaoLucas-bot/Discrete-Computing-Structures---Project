import models.gf_elements as elements

def create_gf_inverse():
    return []

def next_tick(q, a1, a2, a3, b1, b2, b3):
    return [(a1-q*b1), (a2-q*b2), (a3-q*b3)]

def extended_euclid(gf_table, a3, b3):
    (q, a1, a2, b1, b2) = (0, 1, 0, 0, 1)
    while b3 > 1:
        gf_table.append(elements.add_line(q, a1, a2, a3, b1, b2, b3))
        q = a3 // b3
        t = next_tick(q, a1, a2, a3, b1, b2, b3)
        (a1, a2, a3) = (b1, b2, b3)
        (b1, b2, b3) = (t[0], t[1], t[2])
    gf_table.append(elements.add_line(q, a1, a2, a3, b1, b2, b3))
    result = {}
    if gf_table[-1]["B3"] == 1:
        if gf_table[-1]["B2"] >= 0:
            result["MI"] = gf_table[-1]["B2"]
        else:
            result["MI"] = gf_table[-1]["B2"] + gf_table[0]['A3']
    else:
        result["MDC"] = gf_table[-1]["A3"]
    return result  
