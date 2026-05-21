from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent
CSV_PATH = BASE / "data" / "dados_clientes.csv"

try:
    df = pd.read_csv(CSV_PATH)
    print("\n--- Análise de Dados de Clientes ---")
    print("DataFrame Original:")
    print(df)
    media_idade = df["Idade"].mean()
    media_renda = df["Renda"].mean()
    print(f"\nMédia de Idade: {media_idade:.2f} anos")
    print(f"Média de Renda: R$ {media_renda:.2f}")
    cidade_mais_clientes = df["Cidade"].value_counts().idxmax()
    print(f"\nCidade com o maior número de clientes: {cidade_mais_clientes}")
    renda_minima = float(input("\nDigite a renda mínima para filtrar clientes: R$ "))
    clientes_alta_renda = df[df["Renda"] > renda_minima]
    print(f"\nClientes com renda acima de R$ {renda_minima:.2f}:")
    print(clientes_alta_renda)
except FileNotFoundError:
    print(f"Erro: O arquivo '{CSV_PATH}' não foi encontrado.")
except KeyError as e:
    print(f"Erro: Coluna {e!r} não encontrada no arquivo CSV. Verifique o cabeçalho.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
