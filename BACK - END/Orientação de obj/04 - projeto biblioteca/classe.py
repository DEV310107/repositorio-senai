#Cria a classe cliente, onde será adicionado as informações de cada cliente.
class Cliente:
    def __init__(self, nome, email, senha, telefone, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.cpf = cpf
        self.reservas = []  # lista para armazenar os livros que estão reservados



    #adiciona um livro a lista de reservas do cliente
    def reservar_livro(self, livro):
        self.reservas.append(livro)


    #lista todos os livros que estão reservados pelo cliente
    def listar_reservas(self):
        return self.reservas
     
    

#classe do bibliotecario que gerencia os livros 
class Bibliotecario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha


    #adiciona um livro ns lista de livros 
    def adicionar_livro(self, lista_livros, nome, genero, classificacao):
        livro = Livro(nome, genero, classificacao)
        lista_livros.append(livro)
    


#Cria a classe livro, onde será adicionado as instâncias com as informações do livros.
class Livro:
    def __init__(self, titulo, genero, classificacao, reservado=False):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.reservado = reservado
#cria uma instancia para colocar o titulo do livro
    def getTitulo(self):
        return self.titulo
    def setTitulo(self, titulo):
        self.titulo = titulo
#cria uma instancia para colocar o gênero do livro
    def getGenero(self):
        return self.genero
    def setTitulo(self, genero):
        self.genero = genero
#cria uma instancia para colocar a classificação do livro
    def getClassificacao(self):
        return self.classificacao
    def setTitulo(self, classificacao):
        self.classificacao = classificacao

    #mostra se o livro foi reservado ou não
    def getReservado(self):
        return self.reservado
    def setTitulo(self, reservado):
        self.reservado = reservado
    

    def reservar(self):
        self.reservado = True

    def __str__(self):
        return f"{self.titulo} - {self.genero} - Classificação: {self.classificacao} - Reservado: {'sim' if self.reservado else 'não'}"
