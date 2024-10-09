class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        numero = numero
        complemento = complemento
        cep = cep
        cidade = cidade

        # VALIDAÇÕES

        def _verificar_logradouro(self, logradouro):
         self._verificar_nome_tipo_invalido(logradouro)
         self._verificar_nome_vazio_invalido(logradouro)

         self.nome = logradouro
         return self.logradouro