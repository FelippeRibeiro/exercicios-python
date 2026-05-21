import csv
from pathlib import Path


def analisar_vendas(caminho_arquivo):
    total_vendas = 0
    produtos_vendidos = {}
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                produto = linha["produto"]
                quantidade = int(linha["quantidade"])
                preco = float(linha["preco"])
                total_vendas += quantidade * preco
                produtos_vendidos[produto] = produtos_vendidos.get(produto, 0) + quantidade
        if produtos_vendidos:
            produto_mais_vendido = max(produtos_vendidos, key=produtos_vendidos.get)
            qtd = produtos_vendidos[produto_mais_vendido]
            print("\n--- Análise de Vendas ---")
            print(f"Total de vendas: R$ {total_vendas:.2f}")
            print(f"Produto mais vendido: {produto_mais_vendido} ({qtd} unidades)")
        else:
            print("Nenhum dado de vendas encontrado.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except KeyError as e:
        print(f"Erro: Coluna {e!r} não encontrada no arquivo CSV. Verifique o cabeçalho.")
    except ValueError as e:
        print(f"Erro de conversão de dados: {e}. Verifique os valores numéricos no CSV.")
    except OSError as e:
        print(f"Ocorreu um erro inesperado: {e}")


BASE = Path(__file__).resolve().parent
analisar_vendas(BASE / "data" / "vendas.csv")
