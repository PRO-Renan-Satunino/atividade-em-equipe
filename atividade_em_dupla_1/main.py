from models.abstracts.funcionario import Funcionario
from models.endereco import Endereco

endereco1 = Endereco("Rua das flores", 22, "Mansao Ueine", "222222", "Gota Citi")
funcionario1 = Funcionario("Batman", "222222", "brusueine@gmail.com", endereco1)

print(funcionario1)