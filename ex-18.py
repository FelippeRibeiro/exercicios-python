import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).resolve().parent

data = {
    "Nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"],
    "Idade": [28, 35, 22, 40, 30, 25, 33],
    "Cidade": [
        "São Paulo",
        "Rio de Janeiro",
        "São Paulo",
        "Belo Horizonte",
        "Rio de Janeiro",
        "São Paulo",
        "Curitiba",
    ],
    "Renda": [5000.00, 7500.00, 3000.00, 9000.00, 6000.00, 4500.00, 8000.00],
}

df_vis = pd.DataFrame(data)

should_show = os.name == "nt" or bool(os.environ.get("DISPLAY"))

out1 = BASE / "clientes_por_cidade.png"
plt.figure(figsize=(10, 6))
df_vis["Cidade"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Número de Clientes por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Número de Clientes")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--")
plt.tight_layout()
plt.savefig(out1)
if should_show:
    try:
        plt.show()
    except Exception:
        pass
plt.close()

out2 = BASE / "distribuicao_idades.png"
plt.figure(figsize=(10, 6))
plt.hist(df_vis["Idade"], bins=5, color="lightcoral", edgecolor="black")
plt.title("Distribuição de Idades dos Clientes")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.grid(axis="y", linestyle="--")
plt.tight_layout()
plt.savefig(out2)
if should_show:
    try:
        plt.show()
    except Exception:
        pass
plt.close()

print(f"Gráficos '{out1.name}' e '{out2.name}' gerados em {BASE}.")
