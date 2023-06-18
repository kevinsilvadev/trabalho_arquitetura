class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionarLivro(self, livro):
        if livro.EstaDisponivel():
            self.livros.append(livro)
            print(f"Livro '{livro.obterTitulo()}' adicionado à biblioteca.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não está disponível.")

    def removerLivro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.obterTitulo()}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não está na biblioteca.")
    def buscarLivro(self, titulo):
        for livro in self.livros:
            if livro.obterTitulo() == titulo:
                if livro.obterTitulo() == titulo:
                    return livro
        return None

    def adicionarUsuario(self, usuario):
        if usuario.ObterNome() != "":
            self.usuarios.append(usuario)
            print(f"Usuário '{usuario.ObterNome()}' adicionado à biblioteca.")
        else:
            print("Nome de usuário inválido.")

    def removerUsuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuário '{usuario.ObterNome()}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.ObterNome()}' não está registrado na biblioteca.")

    def buscarUsuario(self, nome):
        for usuario in self.usuarios:
            if usuario.ObterNome() == nome:
                if usuario.ObterNome() == nome:
                    return usuario
        return None