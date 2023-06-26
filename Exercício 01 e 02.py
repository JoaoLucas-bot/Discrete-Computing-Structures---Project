#2. Implemente uma função que receba um número inteiro positivo e devolva uma 
#lista com os respectivos factores primos.

def fator_primo(y):
    fatores_primos = []
    divisor = 2
    while divisor <= y:
        if y%divisor == 0:
            fatores_primos.append(divisor)
            y = y/divisor
        else:
            divisor += 1
    return fatores_primos

print(fator_primo(int(input("Indique um valor para calcular os seus fatores primos: "))))


