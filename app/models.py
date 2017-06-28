from django.db import models


class AnotherTeste(models.Model):
    teste = models.CharField(max_length=10)

    def __str__(self):
        return self.teste
