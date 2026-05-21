import datetime
from pathlib import Path


def registrar_log(mensagem, tipo="INFO", nome_arquivo="app.log"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha_log = f"[{timestamp}] [{tipo}] {mensagem}\n"
    caminho = Path(__file__).resolve().parent / nome_arquivo
    with open(caminho, "a", encoding="utf-8") as f:
        f.write(linha_log)


registrar_log("Professor Vagner é top.", "INFO")
registrar_log("Variável 'x' não definida.", "WARNING")
registrar_log("Falha na conexão com o banco de dados.", "ERROR")
print("Logs registrados em 'app.log'.")
