from models.endereco import Endereco
from models.abstracts.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float, crea: str):
        super().__init__(nome, telefone, email, endereco, salario)
        self.crea = self._verificar_crea(crea)
        self.salario = salario
        

    def salario_final(self) -> float:
        bonus = (1.10 * self.salario)
        return bonus

    def _verificar_crea(self, crea: str) -> str:
        self._verificar_crea_vazio_invalido(crea)
        return crea  # Retorna o logradouro validado

    def _verificar_crea_vazio_invalido(self, crea: str) -> None:
        if not crea:
            raise ValueError("Crea não pode ser vazio")
        
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nProfissão: Engenheiro"
            f"\nCrea: {self.crea}"
        )
    
    
       

