listaA = []
listaB = []
listaC = []

for i in range(5):
    listaB.append(int(input("Digite um numero da lista b: ")))
    listaA.append(int(input("Digite um numero da lista a: ")))

for i in range(5):
    listaC.append(listaB[i])
    listaC.append(listaA[i])

print(listaA)
print(listaB)
print(listaC)   
