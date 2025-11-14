class Usuario:
    def __init__(self, id_usuario=None, nome=None, email=None, telefone=None, ativo=True, id=None, **kwargs):
        self.id = id if id is not None else id_usuario
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.ativo = ativo

    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"[{self.id}] {self.nome} | {self.email} | {status}"
