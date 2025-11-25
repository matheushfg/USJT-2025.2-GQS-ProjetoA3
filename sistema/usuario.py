class Usuario:
    def init(self, id_usuario=None, nome=None, email=None, telefone=None, ativo=True, id=None, **kwargs):
        # Garante compatibilidade entre JSON e sistema
        self.id = id if id is not None else id_usuario

        # Dados do usuário
        self.nome = nome
        self.email = email
        self.telefone = telefone

        # Indica se o usuário está ativo no sistema
        self.ativo = ativo

    def str(self):
        # Exibe dados do usuário resumidamente
        status = "Ativo" if self.ativo else "Inativo"
        return f"[{self.id}] {self.nome} | {self.email} | {status}"
