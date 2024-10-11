class Cliente:
      def __init__ (self, nome, senha, tel, email, endereco, genero):
        self.nome = nome
        self.senha = senha
        self.tel = tel
        self.email = email
        self.endereco = endereco
        self.genero = genero


      def getNome(self):
        return self.nome
      def setNome (self, nome):
         self.nome = nome

      def getTel(self):
         return self.tel
      def setTel(self, tel):
         self.tel = tel

      def getEmail(self):
         return self.email
      def setEmail(self, email):
         self.email = email

      def getEndereco(self):
         return self.endereco
      def setEnderco(self, endereco):
         self.endereco = endereco

      def getGenero(self):
         return self.genero
      def setGenero(self, genero):
         self.genero = genero

      def getSenha(self):
         return self.senha
      def setSenha(self, senha):
         self.senha = senha
        
        
class Livro:
    def __init__(self, nome, genero, sinopse, classificacao):
        self.nome = nome
        self.genero = genero
        self.sinopse = sinopse
        self.classificacao = classificacao
        self.reservado = False

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getSinopse(self):
        return self._sinopse

    def setSinopse(self, sinopse):
        self._sinopse = sinopse

    def getClassificacao(self):
        return self._classificacao

    def setClassificacao(self, classificacao):
        self._classificacao = classificacao

    def getReservado(self):
        return self._reservado

    def setReservado(self, reservado):
        self._reservado = reservado