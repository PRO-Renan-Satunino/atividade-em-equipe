from models.endereco import Endereco
from models.abstracts.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, salario: float, crea: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = self._verificar_crea(crea)
        self.salario = self.salario_final(salario)

        def salario_final(self) -> float:
         bonus = (0.10 * self.salario)
        return self.salario_final


    def _verificar_crea(self, crea: str) -> str:
        self._verificar_crea_vazio_invalido(crea)
        return crea  # Retorna o logradouro validado

    def _verificar_crea_vazio_invalido(self, crea: str) -> None:
        if not crea.strip():
            raise ValueError("Crea não pode ser vazio")
        
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nProfissão: Engenheiro"
            f"\nCrea: {self.crea}"
        )
    
    
       

