def gerar_saudacoes(lista_nomes):
    """
    Gera saudações personalizadas para uma lista de nomes.
    """
    saudacoes = []
    for nome in lista_nomes:
        saudacao = f"Olá, {nome}! Seja bem-vindo(a)!"
        saudacoes.append(saudacao)
    return saudacoes

def salvar_em_arquivo(saudacoes, nome_arquivo="saudacoes.txt"):
    """
    Salva as saudações em um arquivo de texto.
    """
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for saudacao in saudacoes:
            arquivo.write(saudacao + "\n")
    print(f"Saudações salvas no arquivo '{nome_arquivo}'.")

def main():
    """
    Função principal do programa.
    """
    # Exemplo de lista de nomes
    lista_nomes = ["Ana", "Carlos", "Beatriz"]

    # Gerar saudações
    saudacoes = gerar_saudacoes(lista_nomes)

    # Exibir saudações no console
    for saudacao in saudacoes:
        print(saudacao)

    # Salvar saudações em um arquivo
    salvar_em_arquivo(saudacoes)

if __name__ == "__main__":
    main()