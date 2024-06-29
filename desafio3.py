import re


def validate_numero_telefone(phone_number):

    padrao = r'\(\d{2}\) 9\d{4}-\d{4}'
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(padrao, phone_number):  
        
      # TODO: Agora crie um return, para retornar que o número de telefone é válido:
      return "Número de telefone válido."
      # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    else:
      return "Número de telefone inválido."
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)