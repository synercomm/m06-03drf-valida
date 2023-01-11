from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


    def validate(self, data):   # validando todos os campos => data nos dá acesso a todas as informações 
        
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve ter 11 digitos"})

        if nome_invalido(data['nome']):
            print(data['nome'])
            raise serializers.ValidationError({'nome':"O Nome deve ter SOMENTE caracteres alfabeticos"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos"})
        
        return data
