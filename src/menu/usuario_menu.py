OPCAO_INVALIDA = "Opção invalida!"


def show_menu(id: int):
    input_usuario: int = -1
    try:
        while input_usuario != 0:
            escolha = input("Menu do Usuário \n"
                            "1 - Listar Livros \n"
                            "2 - Alugar Livro \n"
                            "3 - Listar meus alugueis \n"
                            "4 - Devolver Livro \n"
                            "0 - Sair"
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
                case _:
                    print(OPCAO_INVALIDA)
    except ValueError:
        print(OPCAO_INVALIDA)
