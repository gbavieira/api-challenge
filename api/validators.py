from .models import Receita, Despesa
from rest_framework.validators import ValidationError

def repeticao_receita(data):
    if Receita.objects.filter(descricao=data['descricao'], data__month=data['data'].month, data__year=data['data'].year).exists():
        raise ValidationError('Já existe uma rececita criada com esta descrição neste mês')

def repeticao_despesa(data):
    if Despesa.objects.filter(descricao=data['descricao'], data__month=data['data'].month, data__year=data['data'].year).exists():
        raise ValidationError('Já existe uma despesa criada com esta descrição neste mês')
