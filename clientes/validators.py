def cpf_valido(numero_do_cpf):
    return len(numero_do_cpf) == 11

def nome_invalido(nome):
    return any(char.isdigit() for char in nome)

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9