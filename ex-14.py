def validar_cpf(cpf):
    cpf = "".join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if digito1 != int(cpf[9]):
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if digito2 != int(cpf[10]):
        return False
    return True


cpf_teste = input("Digite um CPF para validar: ")
if validar_cpf(cpf_teste):
    print(f"O CPF {cpf_teste} é VÁLIDO.")
else:
    print(f"O CPF {cpf_teste} é INVÁLIDO.")
