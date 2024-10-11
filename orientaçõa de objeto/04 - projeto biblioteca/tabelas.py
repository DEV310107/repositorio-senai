def listar_livros_dis():
    livro_formatado = []
    limpa_console()
    print("--- LIVROS DISPONÍVEIS ---:")
    cont = 1
    for livro in lista_livros:
        if not livro.reservado:
            livro_formatado.append([livro.getTitulo(), livro.getGenero(), livro.getClassificacao(), livro.getReservado()])
            cont += 1
    print(tabulate(livro_formatado, headers=["Titulo", "Genero", "Classificação", "Reservado"], tablefmt="psql"))