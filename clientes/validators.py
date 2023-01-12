import re                       # expressões regulares p/numeros de telefone
from validate_docbr import CPF  # Algoritmo de Validação do CPF

def cpf_valido(numero_do_cpf):
    cpf = CPF()                 # instancia a classe CPF
    return cpf.validate(numero_do_cpf)

def nome_invalido(nome):
    return any(char.isdigit() for char in nome)

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(numero_celular):
    """Verifica se o formato do numero de celular atende a mascara 11 99999-9999 """
    modelo = '[0-9]:{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta