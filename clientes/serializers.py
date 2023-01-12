from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


    def validate(self, data):   # validando todos os campos => data nos dá acesso a todas as informações 
        
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Numero de CPF invalido"})

        if nome_invalido(data['nome']):
            print(data['nome'])
            raise serializers.ValidationError({'nome':"O Nome deve ter SOMENTE caracteres alfabeticos"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos"})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O numero/formato do celular deve estar no formato 99 99999-9999"})
        
        return data
