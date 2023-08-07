'''
Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
(a) o maior elemento da matriz e sua respectiva posição (linha e coluna);
(b) o menor elemento da matriz e sua respectiva posição.
'''

matriz = []

for l in range(6):
    linha = []
    for col in range(3):
        linha.append(int(input("Digite um numero para a matriz: ")))
    matriz.append(linha)

maior = matriz [0][0]
lin_maior = 0
col_maior = 0
menor = matriz [0][0]
lin_menor = 0
col_menor = 0

for l in range(6):
    for col in range(3):
        if (matriz[l][col]> maior):
            maior = matriz[l][col]
            lin_maior = l
            col_maior = col
        if (matriz[l][col] < menor):
            menor = matriz[l][col]  
            lin_menor = l 
            col_menor = col

for l in range(6):
    print(matriz[l][col])

print(f"O menor elemento da matriz eh {menor:.2f} e esta na linha {lin_menor} e coluna {col_menor}")
print(f"O maior elemento da matriz eh {maior:.2f} e esta na linha {lin_maior} e coluna {col_maior}")         