OPCAO_INVALIDA = "\nOpção invalida! \n"


def menu():
    input_usuario = -1
    while input_usuario != 0:
        try:
            escolha = input("Escolha uma das opções a seguir \n"
                            "1 - Cadastrar usuario \n"
                            "2- Fazer login \n"
                            "0 - Sair \n"
                            ">>> ")
            input_usuario = int(escolha)

            match input_usuario:
                case 0:
                    break
                case 1:
                    print("Cadasto de usuário")
                case 2:
                    print("Fazer login")
                case _:
                    print(OPCAO_INVALIDA)
        except ValueError:
            print(OPCAO_INVALIDA)


if __name__ == '__main__':
    menu()
