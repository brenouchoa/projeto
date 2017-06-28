from django.test import TestCase

from app.models import AnotherTeste


class TesteCase(TestCase):
    def setUp(self):
        AnotherTeste.objects.create(teste="Teste")
        a = AnotherTeste()

    def test_basico(self):
        teste = AnotherTeste.objects.get(teste="Teste")
        self.assertEqual(teste.teste, 'Teste')
        self.assertEqual(teste.__str__(), 'Teste')
        self.assertEqual(str(teste), 'Teste')
