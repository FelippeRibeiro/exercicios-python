import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def extrair_titulos_noticias(url, nome_arquivo="noticias.txt"):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        titulos = soup.find_all("h2")
        caminho = Path(__file__).resolve().parent / nome_arquivo
        with open(caminho, "w", encoding="utf-8") as f:
            for titulo in titulos:
                texto_titulo = titulo.get_text(strip=True)
                if texto_titulo:
                    f.write(texto_titulo + "\n")
        print(f"Títulos de notícias extraídos e salvos em '{caminho}'.")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ou HTTP: {e}")
    except OSError as e:
        print(f"Erro ao gravar arquivo: {e}")

url ="https://g1.globo.com/"
out = "noticias.txt"

