

class ContaBancaria:

  #Função para inserir usuario.
  def __init__(self, titular):
    self.titular = titular
    self.saldo=0
    self.transacoes = []

  #Função de depósito.
  def depositar(self,valor):
    self.saldo+=valor
    self.transacoes.append(f"Deposito + R${valor:.2f}")
    
  #Função de saque.  
  def sacar(self,valor):
    if(valor<=self.saldo):
      self.saldo-=valor
      self.transacoes.append(f"Saque - R${valor:.2f}")
    else:
      print("Você não possue saldo suficiente.")
    
  #Função de extrato.  
  def extrato(self):
      print(f"\nExtrato de {self.titular}:")
      for t in self.transacoes:
       print(t)
      print(f"\nSaldo atual: R${self.saldo:.2f}")

#Chamada das funções.
conta = ContaBancaria("David") 
conta.depositar(100)
conta.sacar(110)
conta.depositar(1000)
conta.sacar(150)
conta.extrato()
