
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.livros_emprestados = []

    def obterNome(self):
        return self.nome

    def obterEmail(self):
        return self.email

    def emprestarLivro(self, livro):
        if livro.estaDisponivel():
            self.livros_emprestados.append(livro)
            livro.definirDisponibilidade(False)
            print(f"Livro '{livro.obterTitulo()}' emprestado para {self.nome}.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não está disponível.")

    def DevolverLivro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.definirDisponibilidade(True)
            print(f"Livro '{livro.obterTitulo()}' devolvido por {self.nome}.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não foi emprestado por {self.nome}.")
