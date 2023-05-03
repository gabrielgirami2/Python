lista = []
lista_par = []
lista_impar = []

for i in range(5):
    num = int(input("Digite um numero: "))
    lista.append(num)

for i in range(5):
    if (lista[i] % 2 == 0):
        lista_par.append(lista[i])    
    else:
        lista_impar.append(lista[i])    

print(lista)
print(lista_par)
print(lista_impar)        