from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Receita, Despesa
from .validators import *

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
    
    def create(self,data):
        repeticao_receita(data)
        return Receita.objects.create(**data)

    def update(self,receita, data):
        repeticao_receita(data)
        receita.descricao = data.get('descricao', receita.descricao)
        receita.valor = data.get('valor', receita.valor)
        receita.data = data.get('data', receita.data)
        receita.save()
        return receita

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

    def create(self,data):
        repeticao_despesa(data)
        return Despesa.objects.create(**data)
    
    def update(self,despesa, data):
        repeticao_despesa(data)
        despesa.descricao = data.get('descricao', despesa.descricao)
        despesa.valor = data.get('valor', despesa.valor)
        despesa.data = data.get('data', despesa.data)
        despesa.save()
        return despesa
