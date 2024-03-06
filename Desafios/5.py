# Desafio 5

def inverter_string(input_string):
    
    caracteres = list(input_string)

    caracteres = caracteres[::-1]

    string_invertida = ''.join(caracteres)

    return string_invertida

string_original = input('Digite uma string para inverter: ')
string_invertida = inverter_string(string_original)

print(f'A string original: {string_original}')
print(f'A string invertida: {string_invertida}')
