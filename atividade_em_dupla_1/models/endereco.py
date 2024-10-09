class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    # VALIDAÇÕES

    def _verificar_logradouro(self, logradouro: str) -> str:
        self._verificar_nome_tipo_invalido(logradouro)
        self._verificar_nome_vazio_invalido(logradouro)
        return logradouro  # Retorna o logradouro validado

    def _verificar_nome_tipo_invalido(self, logradouro: str) -> None:
        if not isinstance(logradouro, str):
            raise ValueError("Logradouro deve ser um nome")
        
    def _verificar_nome_vazio_invalido(self, logradouro: str) -> None:
        if not logradouro.strip():
            raise ValueError("Logradouro não pode ser vazio")
    

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNumero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
        )
    