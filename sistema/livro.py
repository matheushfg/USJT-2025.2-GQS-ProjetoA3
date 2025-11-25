class Livro:
    def __init__(self, id_livro=None, titulo=None, autor=None, isbn=None, ano=None, disponivel=True, id=None, **kwargs):
        # Garante compatibilidade entre ID salvo no JSON e ID interno
        self.id = id if id is not None else id_livro

        # Armazena informações do livro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano

        # Indica se o livro pode ser emprestado
        self.disponivel = disponivel

    def __str__(self):
        # Exibe status do livro
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.id}] {self.titulo} - {self.autor} ({self.ano}) | {status}"
