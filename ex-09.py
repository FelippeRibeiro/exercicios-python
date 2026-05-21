def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))
if numero < 0:
    print("Fatorial não é definido para números negativos.")
else:
    print(f"O fatorial de {numero} é {fatorial(numero)}.")
