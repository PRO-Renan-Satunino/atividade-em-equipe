from models.abstracts.funcionario import Funcionario
from models.endereco import Endereco
from models.medico import Medico
from models.engenheiro import Engenheiro

endereco1 = Endereco("Rua das flores", 22, "Mansao Ueine", "222222", "Gota Citi")
funcionario1 = Funcionario("Batman", "222222", "brusueine@gmail.com", endereco1)
medico1 = Medico("22", "Jair M Bolsonaro", "22 22222 - 2222", "mitogamer22@yahoo.com", endereco1 )
engenheiro1 = Engenheiro("13", "Lula da Silva", "13 1313-1313", "ladraogamer13@gmail.com", endereco1 )

print(funcionario1)
print("\n")
print(medico1)
print(engenheiro1)