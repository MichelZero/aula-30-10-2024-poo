#
# autor: Michel
# data: 30/10/2024

class Veiculo:
  def __init__(self, tipo, cor, placa, numPortas):
    self.tipo = tipo
    self.cor = cor
    self.placa = placa
    self.numPortas = numPortas
    
  #getters
  @property
  def tipo(self):
    return self._tipo
    
  @property
  def cor(self):
      return self._cor
    
  @property
  def placa(self):
      return self._placa
    
  @property
  def numPortas(self):
      return self._numPortas
    
  #setters
  @tipo.setter
  def tipo(self, tipo):
      self._tipo = tipo
      
  @cor.setter
  def cor(self, cor):
      self._cor = cor
      
  @placa.setter
  def placa(self, placa):
      self._placa = placa
      
  @numPortas.setter
  def numPortas(self, numPortas):
      self._numPortas = numPortas
      
  def __str__(self):
      return f"Tipo: {self.tipo}\nCor: {self.cor}\nPlaca: {self.placa}\nNúmero de portas: {self.numPortas}"


# classe veiculo nacional
class VeiculoNacional(Veiculo):
  def __init__(self, tipo, cor, placa, numPortas, preco):
     super().__init__(tipo, cor, placa, numPortas)
     self.preco = preco
     
  #getter
  @property
  def preco(self):
    return self._preco
  
  #setter
  @preco.setter
  def preco(self, value):
    self._preco = value
    
  def __str__(self):
     return f"{super().__str__()}\nPreço: R${self.preco:.2f}"

# classe veiculo importado
class VeiculoImportado(Veiculo):
  def __init__(self, tipo, cor, placa, numPortas, preco):
     super().__init__(tipo, cor, placa, numPortas)
     self.preco = preco
     
  #getter
  @property
  def preco(self):
    return self._preco
  
  #setter
  @preco.setter
  def preco(self, value):
    self._preco = value
    
  def __str__(self):
    return f"{super().__str__()}\nPreço: R${self.preco:.2f}\nImposto: R${self.preco*0.3:.2f}"   
