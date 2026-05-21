import random
import string


def gerar_senha(
    tamanho,
    incluir_maiusculas=True,
    incluir_minusculas=True,
    incluir_numeros=True,
    incluir_especiais=True,
):
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation
    if not caracteres:
        return "Erro: Nenhuma opção de caractere selecionada."
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


tam = int(input("Tamanho da senha: "))
mai = input("Incluir maiúsculas? (s/n): ").lower() == "s"
incluir_minusculas = input("Incluir minúsculas? (s/n): ").lower() == "s"
num = input("Incluir números? (s/n): ").lower() == "s"
esp = input("Incluir especiais? (s/n): ").lower() == "s"
senha_gerada = gerar_senha(tam, mai, incluir_minusculas, num, esp)
print(f"Senha gerada: {senha_gerada}")
