from sistema.livro import Livro
from sistema.usuario import Usuario
from sistema.emprestimo import Emprestimo


class FabricaObjetos:
    """
    Factory Method: responsável pela criação de objetos do sistema.
    Permite centralizar e padronizar a forma como livros, usuários
    e empréstimos são criados, diminuindo acoplamento e facilitando
    extensões futuras.
    """

    @staticmethod
    def criar_livro(id_livro, titulo, autor, isbn, ano):
        return Livro(
            id_livro=id_livro,
            titulo=titulo,
            autor=autor,
            isbn=isbn,
            ano=ano
        )

    @staticmethod
    def criar_usuario(id_usuario, nome, email, telefone):
        return Usuario(
            id_usuario=id_usuario,
            nome=nome,
            email=email,
            telefone=telefone
        )

    @staticmethod
    def criar_emprestimo(id_emp, usuario_id, livro_id):
        return Emprestimo(
            id_emp=id_emp,
            usuario_id=usuario_id,
            livro_id=livro_id
        )
