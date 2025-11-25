from datetime import datetime, timedelta

class Emprestimo:
    def __init__(
        self,
        id_emp=None,
        usuario_id=None,
        livro_id=None,
        data_emp=None,
        devolvido=False,
        data_devolucao=None,
        data_devolucao_real=None,
        id=None,
        **kwargs
    ):
        # Garante compatibilidade de IDs entre JSON e sistema
        self.id = id if id is not None else id_emp

        # Registra IDs do usuário e do livro
        self.usuario_id = usuario_id
        self.livro_id = livro_id

        # Data do empréstimo (hoje por padrão)
        self.data_emprestimo = data_emp or datetime.now().strftime('%Y-%m-%d')
        # Data prevista para devolução (14 dias após o empréstimo)
        self.data_devolucao = data_devolucao or (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

        # Indica se o livro já foi devolvido
        self.devolvido = devolvido
        # Registra a data real da devolução
        self.data_devolucao_real = data_devolucao_real

    def devolver(self):
        # Marca o empréstimo como concluído
        self.devolvido = True
        # Registra a data da devolução
        self.data_devolucao_real = datetime.now().strftime('%Y-%m-%d')

    def __str__(self):
        # Exibe status do empréstimo
        status = "Devolvido" if self.devolvido else "Em andamento"
        return f"[{self.id}] Usuário {self.usuario_id} - Livro {self.livro_id} | {status}"
