from unittest import TestCase


class TestDbFake(TestCase):
    """
    para executar os testes:
    python -m unittest .\teste.py
    """
    def test_acesso_inicial(self):
        resultado  = True
        assert resultado