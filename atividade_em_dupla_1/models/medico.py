from models.endereco import Endereco
from models.abstracts.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, crm: str, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = self._verificar_crm(crm)



    def _verificar_crm(self, crm: str) -> str:
        self._verificar_crm_vazio_invalido(crm)
        return crm  # Retorna o logradouro validado

    def _verificar_crm_vazio_invalido(self, crm: str) -> None:
        if not crm.strip():
            raise ValueError("Crm não pode ser vazio")
        
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nProfissão: Médico"
            f"\nCrm: {self.crm}"
        )
    
    
       

