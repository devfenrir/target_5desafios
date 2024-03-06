# Desafio 2

def ver_fibonacci(numero):
    num1, num2 = 0, 1
    
    while num2 < numero:
        num1, num2 = num2, num1 + num2
        
    if num2 == numero:
        return True
    else:
        return False

input_num = int(input('Informe um número para verificar se pertence à sequência de Fibonacci: '))

if ver_fibonacci(input_num):
    print(f'{input_num} pertence à sequência de Fibonacci.')
else:
    print(f'{input_num} não pertence à sequência de Fibonacci.')