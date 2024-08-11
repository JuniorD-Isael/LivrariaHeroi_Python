OPCAO_INVALIDA = "Opção invalida!"


def show_menu(id: int):
    input_usuario: int = -1
    try:
        while input_usuario != 0:
            escolha = input("Menu do administrador"
                            "1  - Alugar livro"
                            "2  - Devolver livro"
                            "3  - Verificar alugueis"
                            "4  - Listar livros"
                            "5  - Deletar livros"
                            "6  - Atualizar livros"
                            "7  - Listar usuários"
                            "8  - Buscar usuários"
                            "9  - Cadastrar usuários"
                            "10  - Atualizar usuários"
                            "11 - Deletar usuários"
                            "0  - Sair"
                            )
            input_usuario = int(escolha)

            match input_usuario:
                case 0:
                    pass
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    pass
                case 9:
                    pass
                case 10:
                    pass
                case 11:
                    pass
                case _:
                    print(OPCAO_INVALIDA)
    except ValueError:
        print(OPCAO_INVALIDA)
