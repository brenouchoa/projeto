from django.test import TestCase

from app.models import AnotherTeste


class TesteCase(TestCase):
    def setUp(self):
        AnotherTeste.objects.create(teste="Teste")

    def test_basico(self):
        teste = AnotherTeste.objects.get(teste="Teste")
        self.assertEqual(teste.teste, 'Teste')
