from django.db import models
from django.http import HttpResponse


# Create your models here.
class User:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def hello(request):
        return HttpResponse(f"Hello {nome}")
