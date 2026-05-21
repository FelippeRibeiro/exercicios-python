from pathlib import Path


def ler_arquivo(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        print("\n--- Conteúdo do Arquivo ---")
        print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
    except OSError as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


BASE = Path(__file__).resolve().parent
padrao = BASE / "data" / "exemplo.txt"
nome_do_arquivo = input(
    f"Digite o nome do arquivo de texto (Deixe vazio para abrir o arquivo '{padrao.name}' em data/): "
).strip()
caminho = Path(nome_do_arquivo) if nome_do_arquivo else padrao
if not caminho.is_absolute():
    caminho = BASE / caminho
ler_arquivo(caminho)
