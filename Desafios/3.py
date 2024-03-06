# Desafio 3

def sequencia(n, tipo): #calcular e retornar o valor da sequência
  if tipo == 1:
    return n + 2
  elif tipo == 2:
    return 2 ** n
  elif tipo == 3:
    return n ** 2
  elif tipo == 4:
    return (2 * n) ** 2
  elif tipo == 5:
    if n <= 1:
      return n
    else:
      return sequencia(n - 1, 5) + sequencia(n - 2, 5)
  else:
    return None

for i in range(1, 6):
  numero = 7 if i == 1 else 8
  print(f'Sequência {i}:')
  print(f'Elemento {numero}: {sequencia(numero, i)}')

