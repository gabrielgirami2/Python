def main():
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))
    
    matriz_carregada = carregar_matriz(num_linhas, num_colunas)
    media = calcular_media_matriz(matriz_carregada)
    
    print("Matriz carregada:")
    for linha in matriz_carregada:
        print(linha)
    
    print("Média dos elementos da matriz:", media)

def carregar_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f"Digite o elemento da posição ({i}, {j}): "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def calcular_media_matriz(matriz):
    total_elementos = 0
    soma_elementos = 0
    
    for linha in matriz:
        total_elementos += len(linha)
        soma_elementos += sum(linha)
    
    media = soma_elementos / total_elementos
    return media

if __name__ == "__main__":
    main()