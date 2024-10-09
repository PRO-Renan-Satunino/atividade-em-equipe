import pytest
from models.endereco import Endereco

@pytest.fixture
def endereco1():
    return Endereco("Rua das flores", 22, "Brusueine", "2222-222", "SalvaCity")