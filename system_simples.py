import datetime

usuarios = {}
usuarios_contas = {}

class ContaBancaria:

  #Função para inserir usuario.
  def __init__(self, titular):
    self.titular = titular
    self.saldo=0
    self.transacoes = []
    self.limite_transacoes = 10
    self.data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

  #Função de depósito.
  def depositar(self,valor):
    if len(self.transacoes)<self.limite_transacoes:
      self.saldo+=valor
      self.transacoes.append(f"Deposito + R${valor:.2f} {self._hora_atual()}")
    else:  
      print(f"Limite de transações atingido. Não é possível adicionar mais transações.{self._hora_atual()}")
    
    
  #Função de saque.  
  def sacar(self,valor):
    if len(self.transacoes)<self.limite_transacoes:
      if(valor<=self.saldo):
        self.saldo-=valor
        self.transacoes.append(f"Saque - R${valor:.2f} {self._hora_atual()}")
      else:
        print("Você não possue saldo suficiente.")
    else:
      print(f"Limite de transações atingido. Não é possível adicionar mais transações.{self._hora_atual()}")
    
  #Função de extrato.  
  def extrato(self):
      print(f"\nExtrato de {self.titular}:")
      for t in self.transacoes:
       print(t)
      print(f"\nSaldo atual: R${self.saldo:.2f}")

  def _hora_atual(self):
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Dados do usuário
class Pessoa:
  def __init__(self):
      self.nome = input("Digite o nome do titular da conta: ")
      self.data_nascimento = input("Digite a data de nascimento do titular da conta: ")
      self.cpf = input("Digite o CPF do titular da conta: ")
      self.conta = []

  def __str__(self):
     return f"👤 Titular: {self.nome}, 🗓️ Nascimento: {self.data_nascimento}, 🆔 CPF: {self.cpf}"

# Dados da conta
class Conta:
  def __init__(self):
    self.agencia = input("Digite a agência: ")
    self.numero = input("Digite o número da conta: ")

  def __str__(self):
    return f"🏦 Agência: {self.agencia}, 📄 Conta: {self.numero}"

# Dados do endereço
class Endereco:
  def __init__(self):
    self.logradouro = input("Digite o logradouro: ")
    self.numero = input("Digite o número: ")
    self.bairro = input("Digite o bairro: ")
    self.cidade = input("Digite a cidade: ")
    self.estado = input("Digite o estado: ")

  def __str__(self):
    return f"Endereço: {self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado}"



# Função de cadastro de usuário
def cadastrar_usuario():
     # Criação do objeto Pessoa, que agora pede os dados diretamente
    pessoa = Pessoa()

    if pessoa.cpf in usuarios:
        print("⚠️ Usuário já cadastrado com este CPF!")
        return

    # Armazenando o usuário no dicionário com o CPF como chave
    usuarios[pessoa.cpf] = pessoa
    print(f"✅ Usuário {pessoa.nome} cadastrado com sucesso!")

# Função de cadastro de conta
def cadastrar_conta():
# Função de cadastro de conta
  conta = Conta()

  cpf = input("Digite o CPF do titular da conta para associar: ")
  if cpf not in usuarios:
    print("⚠️ Usuário não encontrado com esse CPF!")
    return

  if conta.numero in usuarios_contas:
     print("⚠️ Conta já cadastrada!")
     return
  
  if cpf in usuarios_contas:
    usuarios_contas[cpf].append(conta)

  usuarios_contas[conta.numero] = conta
  print(f"✅ Conta {conta.numero} cadastrada com sucesso!")

# Função de seleção de usuário
def selecionar_usuario():
    cpf = input("Digite o CPF do usuário: ")
    if cpf not in usuarios:
        print("⚠️ Usuário não encontrado!")
        return None
    return usuarios[cpf]

# Função de listar usuários
def listar_usuarios():
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
        return
    
    print("\n📜 Usuários cadastrados:")
    for cpf, pessoa in usuarios.items():
        print(pessoa)

# Função de seleção de conta
def selecionar_conta():
    numero = input("Digite o número do conta: ")
    conta = usuarios_contas.get(numero)
    if conta is None:
        print("⚠️ Conta não encontrado!")
        return None
    return conta

# Função de listar contas
def listar_contas():
    if not usuarios_contas:
        print("📭 Nenhuma conta cadastrada.")
        return
    
    print("\n📜 Contas cadastrados:")
    for agencia, numero in usuarios_contas.items():
        print(numero)

# Função principal
def main():
    while True:
        print("\n=== 🏦 MENU ===")
        print("1 - Cadastrar usuário")
        print("2 - Selecionar usuário e acessar conta")
        print("3 - Listar usuários cadastrados")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = selecionar_usuario()
            if usuario:
                print(f"\n===👤 BEM-VINDO AO BANCO {usuario.nome}===")
                menu_usuario(usuario)
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "4":
            print("👋 Saindo... Obrigado por usar nosso sistema!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

def menu_usuario(usuario):
    while True:
        print("\n=== 💳 MENU CONTA CORRENTE ===")
        print("1 - criar conta")
        print("2 - Selecionar conta e acessar")
        print("3 - Listar contas cadastrados")
        print("4 - Retornar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_conta()
        elif opcao == "2":
            conta = selecionar_conta()
            if conta:
                menu_conta(conta)
        elif opcao == "3":
            listar_contas()
        elif opcao == "4":
            print("🔙 Retornando ao menu principal...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")


# Função para interagir com a conta do usuário
def menu_conta(conta):
    while True:
        print("\n=== 💳 MENU CONTA ===")
        print("1️⃣ - Depositar")
        print("2️⃣ - Sacar")
        print("3️⃣ - Extrato")
        print("4️⃣ - Voltar ao menu Conta Corrente")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.extrato()
        elif opcao == "4":
            print("🔙 Retornando ao menu principal...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")


# Iniciando o programa
if __name__ == "__main__":
    main()

