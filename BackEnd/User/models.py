import re

from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError

from utils.validacpf import valida_cpf


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11, verbose_name='Número de telefone')
    email =  models.EmailField(max_length=254) 
    address = models.CharField(max_length=50, verbose_name='Endereço')
    address_number = models.CharField(max_length=5, verbose_name='Número de endereço')
    complement = models.CharField(max_length=30, verbose_name='Complemento')
    district = models.CharField(max_length=30, verbose_name='Bairro')
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30, verbose_name='Cidade')
    state = models.CharField(
        verbose_name='Estado',
        max_lenght=2,
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def clean(self):
        error_messages = {}

        cpf_sent = self.cpf or None
        cpf_saved = None
        profile = Profile.objects.filter(cpf=cpf_sent).first()

        if profile:
            cpf_saved = profile.cpf

            if cpf_saved is not None and self.pk != profile.pk:
                error_messages['cpf'] = 'CPF já existe.'

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'CEP inválido, digite os 8 digitos do CEP.'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'