#----------------------------------------#
 
# Chamada da classe Livro:
import datetime
import os
import sys
 
 
class Livro:
    def __init__(self, titulo, autor, ano, genero, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.disponibilidade = disponibilidade
       
#----------------------------------------#
 
# Chamada da classe Usuários:    
class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
       
#----------------------------------------#
 # Classe para o empréstimo de livros de usuário para usuário:
class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo, data_devolucao):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
 
#----------------------------------------#
 
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    #Empresta um livro a um usuário.
    def emprestar_livro(self, livro, usuario):
        
        

        
        # Verifica se o livro está disponível
        for liv in self.livros:
            if liv.titulo.lower() == livro.lower() and liv.disponibilidade:
                # Verifica se o usuário está cadastrado
                for user in self.usuarios:
                    if user.nome.lower() == usuario.lower():
                        emprestimo = Emprestimo(user, liv, datetime.date.today(), None)
                        liv.disponibilidade = False
                        print(f"O livro {liv.titulo} foi emprestado para {user.nome} com sucesso!")
                        return
                print("Usuário não cadastrado na biblioteca.")
                return
        print(f"O livro {livro} não está disponível para empréstimo.")

    def listar_livros_disponiveis(self):
        """Lista todos os livros disponíveis na biblioteca."""
        print("**Lista de Livros Disponíveis:**")
        for livro in self.livros:
            if livro.disponibilidade:
                print(f"- {livro.titulo} ({livro.autor})")
        print("\n")

    def listar_livros_emprestados(self):
        """Lista todos os livros atualmente emprestados."""
        print("**Lista de Livros Emprestados:**")
        for livro in self.livros:
            if not livro.disponibilidade:
                print(f"- {livro.titulo} ({livro.autor})")
        print("\n")

    def listar_usuarios(self):
        """Lista todos os usuários cadastrados na biblioteca."""
        print("**Lista de Usuários Cadastrados:**")
        for usuario in self.usuarios:
            print(f"- {usuario.nome} (ID: {usuario.id})")
        print("\n")
       
#----------------------------------------#
 
# Função para reiniciar o Sistema:
 
def reiniciar_aplicativo():
    python = sys.executable
    os.execl(python, python, *sys.argv)
   
#----------------------------------------#
 
print("Bem vindo ao Main da Atividade:")
print("\n")
 
# Criação da biblioteca
biblioteca = Biblioteca()
 
# Opções do menu
print("1 - Adicionar Livro")
print("2 - Adicionar Usuário")
print("3 - Emprestar Livro")
print("4 - Listar Livros Disponíveis")
print("5 - Listar Livros Emprestados")
print("6 - Listar Usuários")
 
print("\n")
 
# Operação principal do programa
while True:
    opcao = int(input("O que você deseja fazer?: "))
 
    print("\n")
 
    # Seleção da função de acordo com a opção escolhida
    if opcao == 1:
        livro = Livro(input("Digite o Título do Livro: "),
                      input("Digite o nome do autor do Livro: "),
                      int(input("Digite o ano de publicação do Livro: ")),
                      input("Digite o gênero correspondente ao Livro: "),
                      True)
        biblioteca.adicionar_livro(livro)
 
    elif opcao == 2:
        usuario = Usuario(int(input("Digite o número de ID do usuário: ")),
                          input("Digite o nome do usuário: "))
        biblioteca.adicionar_usuario(usuario)
 
    elif opcao == 3:
        livro = input("Digite o título do livro que deseja emprestar: ")
        usuario = input("Digite o nome do usuário que deseja emprestar o livro: ")
        biblioteca.emprestar_livro(livro, usuario)
 
    elif opcao == 4:
        biblioteca.listar_livros_disponiveis()
 
    elif opcao == 5:
        biblioteca.listar_livros_emprestados()
 
    elif opcao == 6:
        biblioteca.listar_usuarios()
 
    else:
        print("Opção inválida.")
 
    if input("Deseja voltar ao menu de seleção? (s/n): ").lower() != "s":
        break
 
print("Encerrando o programa...")
 
#----------------------------------------#
