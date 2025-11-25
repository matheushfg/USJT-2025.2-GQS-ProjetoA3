from sistema.livro import Livro
from sistema.usuario import Usuario
from sistema.emprestimo import Emprestimo


class FabricaObjetos:
    """
    Factory Method: responsável por centralizar a criação de objetos
    do sistema (Livro, Usuario, Emprestimo). Facilita manutenção,
    padronização e futuras extensões.
    """

    @staticmethod
    def criar_livro(id_livro, titulo, autor, isbn, ano):
        """Cria e retorna um objeto Livro com os dados fornecidos."""
        return Livro(
            id_livro=id_livro,
            titulo=titulo,
            autor=autor,
            isbn=isbn,
            ano=ano
        )

    @staticmethod
    def criar_usuario(id_usuario, nome, email, telefone):
        """Cria e retorna um objeto Usuario com os dados fornecidos."""
        return Usuario(
            id_usuario=id_usuario,
            nome=nome,
            email=email,
            telefone=telefone
        )

    @staticmethod
    def criar_emprestimo(id_emp, usuario_id, livro_id):
        """Cria e retorna um objeto Emprestimo com usuário e livro associados."""
        return Emprestimo(
            id_emp=id_emp,
            usuario_id=usuario_id,
            livro_id=livro_id
        )
