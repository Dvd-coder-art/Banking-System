import json
import os

#Classe para definir o sistema de conta bancária.
class ContaBancaria:

  #Função para inserir usuario.
  def __init__(self, titular):
    self.titular = titular
    self.saldo=0
    self.transacoes = self.carregar_extrato()

  #Função para carregar o arquivo de extrato.
  def carregar_extrato(self):
        try:
            with open(f"{self.titular}_extrato.txt", "r") as file:
                dados = json.load(file)
                self.saldo = dados["saldo"]
                return dados["transacoes"]
        except FileNotFoundError:
            return [] 
        
  #Função para salvar o arquivo de extrato.
  def salvar_extrato(self):
    caminho = os.path.abspath(f"{self.titular}_extrato.txt")
    with open(caminho, "w") as file:
        json.dump({"saldo": self.saldo, "transacoes": self.transacoes}, file)
    print(f"Extrato salvo em: {caminho}") 

  #Função de depósito.
  def depositar(self,valor):
    self.saldo+=valor
    self.transacoes.append(f"Deposito + R${valor:.2f}")
    
  #Função de saque.  
  def sacar(self,valor):
    self.saldo-=valor
    self.transacoes.append(f"Saque - R${valor:.2f}")
    
  #Função de extrato.  
  def extrato(self):
      print(f"Extrato de {self.titular}:")
      for t in self.transacoes:
       print(t)
      print(f"Saldo atual: R${self.saldo:.2f}")

#Chamada das funções.
conta = ContaBancaria("David") 
conta.depositar(100)
conta.sacar(50)
conta.extrato()
conta.salvar_extrato()
conta.carregar_extrato()