import json
from sistema.livro import Livro
from sistema.usuario import Usuario
from sistema.emprestimo import Emprestimo

class Biblioteca:
    def __init__(self, arquivo_dados='biblioteca.json'):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []
        self.arquivo = arquivo_dados
        self.contador_livros = 1
        self.contador_usuarios = 1

    # ---------- LIVROS ----------
    def adicionar_livro(self, titulo, autor, isbn, ano):
        if not titulo or not autor or not isbn:
            print("Erro: campos obrigatórios")
            return False

        if len(isbn) not in (10, 13):
            print("ISBN inválido")
            return False

        if any(livro.isbn == isbn for livro in self.livros):
            print("Livro já existe")
            return False

        novo_livro = Livro(self.contador_livros, titulo, autor, isbn, ano)
        self.livros.append(novo_livro)
        self.contador_livros += 1
        print("Livro adicionado com sucesso.")
        self.salvar_dados()
        return True

    # ---------- USUÁRIOS ----------
    def cadastrar_usuario(self, nome, email, telefone):
        if not nome or "@" not in email:
            print("Nome ou email inválido")
            return False

        if any(u.email == email for u in self.usuarios):
            print("Email já cadastrado")
            return False

        novo_usuario = Usuario(self.contador_usuarios, nome, email, telefone)
        self.usuarios.append(novo_usuario)
        self.contador_usuarios += 1
        print("Usuário cadastrado com sucesso.")
        self.salvar_dados()
        return True

    # ---------- EMPRÉSTIMOS ----------
    def realizar_emprestimo(self, usuario_id, livro_id):
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        livro = next((l for l in self.livros if l.id == livro_id), None)

        if not usuario:
            print("Usuário não encontrado.")
            return False
        if not livro:
            print("Livro não encontrado.")
            return False
        if not livro.disponivel:
            print("Livro não disponível.")
            return False

        emprestimo = Emprestimo(len(self.emprestimos) + 1, usuario_id, livro_id)
        livro.disponivel = False
        self.emprestimos.append(emprestimo)
        print("Empréstimo realizado com sucesso.")
        self.salvar_dados()
        return True

    def devolver_livro(self, emprestimo_id):
        emprestimo = next((e for e in self.emprestimos if e.id == emprestimo_id), None)
        if not emprestimo:
            print("Empréstimo não encontrado.")
            return False
        if emprestimo.devolvido:
            print("Livro já devolvido.")
            return False

        livro = next((l for l in self.livros if l.id == emprestimo.livro_id), None)
        if livro:
            livro.disponivel = True

        emprestimo.devolver()
        print("Livro devolvido com sucesso.")
        self.salvar_dados()
        return True

    # ---------- LISTAGENS ----------
    def listar_livros(self):
        print("\n=== LIVROS ===")
        for livro in self.livros:
            print(livro)

    def listar_usuarios(self):
        print("\n=== USUÁRIOS ===")
        for usuario in self.usuarios:
            print(usuario)

    def listar_emprestimos(self):
        print("\n=== EMPRÉSTIMOS ===")
        for emp in self.emprestimos:
            print(emp)

    # ---------- PERSISTÊNCIA ----------
    def salvar_dados(self):
        dados = {
            'livros': [vars(l) for l in self.livros],
            'usuarios': [vars(u) for u in self.usuarios],
            'emprestimos': [vars(e) for e in self.emprestimos],
            'contador_livros': self.contador_livros,
            'contador_usuarios': self.contador_usuarios
        }
        with open(self.arquivo, 'w') as f:
            json.dump(dados, f, indent=2)

    def carregar_dados(self):
        try:
            with open(self.arquivo, 'r') as f:
                dados = json.load(f)
                self.livros = [Livro(**l) for l in dados['livros']]
                self.usuarios = [Usuario(**u) for u in dados['usuarios']]
                self.emprestimos = [Emprestimo(**e) for e in dados['emprestimos']]
                self.contador_livros = dados['contador_livros']
                self.contador_usuarios = dados['contador_usuarios']
            print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo de dados não encontrado, iniciando novo.")

# ---------- Execução principal (modo manual) ----------
if __name__ == "__main__":
    sistema = Biblioteca()
    sistema.adicionar_livro("1984", "George Orwell", "9780451524935", 1949)
    sistema.cadastrar_usuario("João Silva", "joao@email.com", "11999999999")
    sistema.listar_livros()

# ===========================================================
# 🔄 Funções de compatibilidade com os testes automatizados
# ===========================================================
"""
Essas funções mantêm compatibilidade com o código legado e com os testes automatizados
(test_sistema.py), que ainda utilizam nomes antigos e chamadas procedurais.

Elas redirecionam as chamadas antigas (ex: adicionarLivro) para os novos
métodos da classe Biblioteca (ex: adicionar_livro).
"""

# Instância global única usada nos testes
_sistema = Biblioteca()

def adicionarLivro(titulo, autor, isbn, ano):
    """Mantém compatibilidade com test_adicionar_livro_valido"""
    return _sistema.adicionar_livro(titulo, autor, isbn, ano)

def cadastrarUsuario(nome, email, telefone):
    """Mantém compatibilidade com test_cadastrar_usuario_valido"""
    return _sistema.cadastrar_usuario(nome, email, telefone)

def realizarEmprestimo(usuario_id, livro_id):
    """Mantém compatibilidade com test_realizar_emprestimo_valido"""
    return _sistema.realizar_emprestimo(usuario_id, livro_id)

def devolverLivro(emprestimo_id):
    """Mantém compatibilidade com test_devolver_livro_valido"""
    return _sistema.devolver_livro(emprestimo_id)

def salvarDados():
    """Mantém compatibilidade com test_salvar_e_carregar_dados"""
    return _sistema.salvar_dados()

def carregarDados():
    """Mantém compatibilidade com test_salvar_e_carregar_dados"""
    return _sistema.carregar_dados()

# Compatibilidade com listas globais e contadores usados nos testes
livros = _sistema.livros
usuarios = _sistema.usuarios
emprestimos = _sistema.emprestimos
contador_livros = _sistema.contador_livros
contador_usuarios = _sistema.contador_usuarios

