lista_numeros = [4, 11, 3, 5, 2, 6, 7, 9]

nova_lista = list(map(lambda num : num + 5 if (num % 2 == 0) else num - 2, lista_numeros))

print(nova_lista)