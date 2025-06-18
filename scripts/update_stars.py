import requests

USUARIO = "CarlosDanielSucre"
URL = f"https://api.github.com/users/{USUARIO}/repos?per_page=100"

resposta = requests.get(URL)
repos = resposta.json()

total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)

# Atualiza o README.md
with open("README.md", "r", encoding="utf-8") as file:
    conteudo = file.read()

import re
novo_conteudo = re.sub(
    r"!\[Estrelas recebidas\]\(https:\/\/img\.shields\.io\/badge\/estrelas-\d+",
    f"![Estrelas recebidas](https://img.shields.io/badge/estrelas-{total_stars}",
    conteudo
)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(novo_conteudo)