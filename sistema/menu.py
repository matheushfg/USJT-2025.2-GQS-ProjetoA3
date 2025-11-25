from sistema.biblioteca import Biblioteca

def menu():
    sistema = Biblioteca()
    sistema.carregar_dados()

    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Adicionar Livro")
        print("2. Cadastrar Usuário")
        print("3. Realizar Empréstimo")
        print("4. Devolver Livro")
        print("5. Listar Livros")
        print("6. Listar Usuários")
        print("7. Listar Empréstimos")
        print("8. Salvar Dados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            ano = int(input("Ano: "))
            sistema.adicionar_livro(titulo, autor, isbn, ano)

        elif opcao == "2":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            sistema.cadastrar_usuario(nome, email, telefone)

        elif opcao == "3":
            usuario_id = int(input("ID do Usuário: "))
            livro_id = int(input("ID do Livro: "))
            sistema.realizar_emprestimo(usuario_id, livro_id)

        elif opcao == "4":
            emprestimo_id = int(input("ID do Empréstimo: "))
            sistema.devolver_livro(emprestimo_id)

        elif opcao == "5":
            sistema.listar_livros()

        elif opcao == "6":
            sistema.listar_usuarios()

        elif opcao == "7":
            sistema.listar_emprestimos()

        elif opcao == "8":
            sistema.salvar_dados()
            print("Dados salvos com sucesso.")

        elif opcao == "0":
            sistema.salvar_dados()
            print("Saindo...")
            break

        else:
            print("Opção inválida")