from testador import get_git

git = get_git()

print(
        "\n\\version \"2.22.2\" \n\\language \"portugues\" \n"
        "\n\\header {\n    title = \"Matheus Prado\""
        f"subtitle = \"Contrapontos de primeira espécie gerados por computador em {dia}\""
        f"composer = \"Versão git: {git}\""
    )