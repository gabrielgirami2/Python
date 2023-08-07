lista = [1,2,3,4,5,6,7,8,9]

print(f"{lista}")

print(f"{lista[5]}")

print(f"{lista.index(6)}")

print(f"{lista[1:4]}")

num = 20

if (num in lista):
    print("Está na lista")
else:
    print("Fora da lista")    

lista.append(20)
print(lista)

lista.pop(9)
print(lista)

print(f"{len(lista)}")

lista_pessoa = ['Maria', 19, 1.75]
print(lista_pessoa)


for i in range(10):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

for i in range(10):
    print(lista[i])

print("\n")


lista_A = []
lista_B = []

for i in range(4):
    number = int(input("Digite um numero: "))
    lista_A.append(number)

for i in range(4):
    dobro = lista_A[i]* 2 
    lista_B.append(dobro)   

print(lista_A)
print(lista_B)