from models.abstracts.funcionario import Funcionario
from models.endereco import Endereco
from models.medico import Medico
from models.engenheiro import Engenheiro

endereco1 = Endereco("Rua das flores", 22, "Mansao Ueine", "222222", "Gota Citi")
medico1 = Medico("Carlos", "(71) 9 8822-1122", "carlinhomed@gmail.com", endereco1, 1000, "22211")
engenheiro1 = Engenheiro("Bob", "(71) 9 8822-1124", "bobtheconstructor@gmail.com", endereco1, 1000, "255522")

print("\n")
print(medico1)
print(engenheiro1)