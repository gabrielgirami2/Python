def main():
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))
    
    matriz_carregada = carregar_matriz(num_linhas, num_colunas)
    
    print("Matriz carregada:")
    for linha in matriz_carregada:
        print(linha)

def carregar_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f"Digite o elemento da posição ({i}, {j}): "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

 
if __name__ == "__main__":
    main()