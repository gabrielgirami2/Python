#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos no teclado. No final, mostre a matriz, com a formatação correta

matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

    print("-=" *30)
    for l in range(0,3):
        for c in range(0,3):
            print(f"[{matriz [l][c]}]", end='')
        print()        