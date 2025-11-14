class Livro:
    def __init__(self, id_livro=None, titulo=None, autor=None, isbn=None, ano=None, disponivel=True, id=None, **kwargs):
        # compatibilidade com JSON ("id") e com código interno ("id_livro")
        self.id = id if id is not None else id_livro

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano

        # compatível com JSON salvo anteriormente
        self.disponivel = disponivel

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.id}] {self.titulo} - {self.autor} ({self.ano}) | {status}"
