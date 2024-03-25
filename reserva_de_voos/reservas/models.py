from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.
class Admin(models.Model):
    nome_admin = models.CharField(max_length=100, default='admin')
    email_admin = models.EmailField(default='admin@gmail.com')
    senha_admin = models.CharField(max_length=255, default='admin123')
    
    def __str__(self):
        return self.nome_admin

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=255, default='senha_padrao')

    @property
    def idade(self):
        today = date.today()
        age = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return age

    def save(self, *args, **kwargs):
        if self.idade < 18:
            raise ValueError("O usuário deve ter mais de 18 anos.") # tem que devolver algo responsivo
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    
class Voo(models.Model):
    id_voo = models.CharField(max_length=100, unique=True)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data = models.DateField()
    horario_saida = models.TimeField()
    horario_chegada = models.TimeField()
    preco_economica = models.DecimalField(max_digits=10, decimal_places=2)
    preco_executiva = models.DecimalField(max_digits=10, decimal_places=2)
    assentos = models.DecimalField(max_digits=10, decimal_places=0, default = '133')

    def __str__(self):
        return f'{self.origem} - {self.destino} ({self.data} - {self.horario_saida} - {self.horario_chegada})'

class Assento(models.Model):
    fileira = models.PositiveSmallIntegerField()  # Pode ser de 1 a 19
    numero = models.CharField(max_length=1)       # Pode ser de "A" a "G"
    classe = models.CharField(max_length=20)      # Pode ser "executiva" ou "economica"
    disponivel = models.BooleanField(default=True)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fileira}{self.numero}"

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    assentos_reservados = models.ManyToManyField(Assento)

    def __str__(self):
        return f'Reserva de {self.usuario} para o voo {self.voo}'

