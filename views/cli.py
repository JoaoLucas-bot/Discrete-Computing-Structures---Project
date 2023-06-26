from controllers import gf_inverse

def cli():
    while True:
        gf_table: list[dict] = gf_inverse.create_gf_inverse()
        numbers: list = input("Indique n e b separados por espaço ou 'exit' para sair: ").split(" ")
        print("")
        if numbers[0] == "exit":
            break
        elif len(numbers) < 2 or len(numbers) > 2:
            print("Necessários dois números inteiros!")
        else:
            try:
                numbers[0] = int(numbers[0])
                numbers[1] = int(numbers[1])
                if int(numbers[1]) > int(numbers[0]):
                    print(f"Erro: b ({numbers[1]}) tem de ser menor ou igual a n ({numbers[0]})")
                else:    
                    result: dict = gf_inverse.extended_euclid(gf_table, int(numbers[0]), int(numbers[1]))
                    print(f"{'Q': <5}{'A1': ^7}{'A2': ^7}{'A3': ^7}{'B1': ^7}{'B2': ^7}{'B3': ^7}")
                    print("-----------------------------------------------")
                    for i in gf_table:
                        print(f"{i['Q']: <5}{i['A1']: ^7}{i['A2']: ^7}{i['A3']: ^7}{i['B1']: ^7}{i['B2']: ^7}{i['B3']: ^7}")
                    if "MI" in result.keys():
                        print(f"Multiplicativo inverso: {result['MI']}")
                        print("")
                    else:
                        print(f"MDC: {result['MDC']}")
                        print("")
            except ValueError:
                print("Necessários dois números inteiros!")
        