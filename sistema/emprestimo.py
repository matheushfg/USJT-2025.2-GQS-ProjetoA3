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
        self.id = id if id is not None else id_emp
        self.usuario_id = usuario_id
        self.livro_id = livro_id

        self.data_emprestimo = data_emp or datetime.now().strftime('%Y-%m-%d')
        self.data_devolucao = data_devolucao or (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

        self.devolvido = devolvido
        self.data_devolucao_real = data_devolucao_real

    def devolver(self):
        self.devolvido = True
        self.data_devolucao_real = datetime.now().strftime('%Y-%m-%d')

    def __str__(self):
        status = "Devolvido" if self.devolvido else "Em andamento"
        return f"[{self.id}] Usuário {self.usuario_id} - Livro {self.livro_id} | {status}"
