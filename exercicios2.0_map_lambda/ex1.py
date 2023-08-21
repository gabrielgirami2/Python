lista_pares = [2, 4, 6, 8, 10]
lista_impar = [1, 3, 5, 7, 9]

soma_pares = list(map(lambda num : sum(lista_pares) if (num % 2 == 0) else num + 1, lista_pares ))

soma_impar = list(map(lambda num : sum(lista_pares) if (num % 2 == 0) else sum(lista_impar), lista_impar ))


print(soma_pares)
print(soma_impar)
