import time
#começo da classe
class Usuario:
# Atributos\instancia
#self sempre remete a propria instancia
  def __init__(self,nome_usu,
               email_usu,
               senha_usu,
               num_usu
              ):
    self.__nome_usu = nome_usu
    self.__email_usu = email_usu
    self.__senha_usu = senha_usu
    self.__num_usu = 0

  # Codigo para inserir\cadastrar o usuario
                #Tentantiva alternativa
def inserir_usuario():
    print('loading...')
    time.sleep(1)
    print( "ʕ•ᴥ•ʔ OLÁ! você veio fazer um cadastro, não é? " '[forneça suas informações! usuário!]')
    time.sleep(2)
    nome_usu = input("Nome: " )
    email_usu = input("Email: ")
    senha_usu = input("Senha:")
    num_usu = int(input("Número: "))
     #substituir essa parte por banco           
    #doc = open('Usuario.txt', 'a+')
    #doc.write(f' nome {self.nome_usu}; email {self.email_usu}; senha {senha_usu}; numero {self.num_usu}\n')
    #doc.close()
    
def consultar_usuario(self):
    print("1")
    # Codigo para consultar as tarefas do usuario
def atualizar_usuario(self):
  novo_nome=input('novo nome')
  self.nome_usu=novo_nome
  print('nome atualizado para: {}'.format(self.senha_usu))
  nova_senha=input('nova senha: ')
  self.senha_usu=nova_senha
  print('senha atualizada para: {}'.format(self.senha_usu))
print('2')
    #  Codigo para modificar o usuario
def excluir_usuario(self):
    print('2')
    # Codigo para excluir o usuario
  
def logar_usuario(self):
    os.system('clear')
    print( "ʕ•ᴥ•ʔ OLÁ DE NOVO! Lembra sua senha, não é? ")
    print( " Forneça os dados de seu login: ")
    emailLog = input("Email: ")
    senhaLog = input("Senha: ")
    doc = open('Usuario.txt')
    usuario = doc.readlines()
    while emailLog not in usuario and senhaLog not in usuario:
      print(+ "...")
      time(1)
      print("Usuário, você errou tudo!ʕ•ᴥ•ʔ ")
      print("Tente mais uma vez!")
      emailLog = input( "Digite email: ")
      senhaLog = input( "Digite a Senha: ")
      os.system('clear')
      #if emailLog == get_line(x) and senhaLog == get_line(x):
        #print('1')
      #('22')
    # Codigo para logar\cadastrar o usuario
    
# Encapsulamento para Ler\acessar (getters)
  #def getNome(self):
   # return self.nome_usu
  #def getEmail(self):
   # return self.email_usu
  #def getSenha(self):
    #return self.senha_usu
  #def getNumero(self):
   # return self.num_usu
# Encapsulamento para modificar\atribuir dentro do obj(setters)
  #def setNome(self,nome_usu):
   #self.__nome_usu=nome_usu
   
  #def setEmail(self,email_usu):
   # self.__email_usu=email_usu
    
  #def setSenha(self,senha_usu):
   # self.__senha_usu=senha_usu
    
  #def setNumero(self,num_usu):
   # self.__num_usu=num_usu

