def main():
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))
    
    matriz_carregada = carregar_matriz(num_linhas, num_colunas)
    
    print("Matriz carregada:")
    for linha in matriz_carregada:
        print(linha)
    
    print("Elementos ímpares da matriz:")
    exibir_elementos_impares(matriz_carregada)


def carregar_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f"Digite o elemento da posição ({i}, {j}): "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def exibir_elementos_impares(matriz):
    for linha in matriz:
        for elemento in linha:
            if elemento % 2 != 0:
                print(elemento)
        print()

if __name__ == "__main__":
    main()
