def main():
    tamanho_lista = int(input("Digite o tamanho da lista: "))
    lista_numerica = ler_lista(tamanho_lista)
    elemento_busca = float(input("Digite o elemento a ser buscado na lista: "))
    indice = buscar_elemento(lista_numerica, elemento_busca)
    
    if indice != -1:
        print(f"O elemento {elemento_busca} foi encontrado na posição {indice} da lista.")
    else:
        print(f"O elemento {elemento_busca} não foi encontrado na lista.")

def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = float(input(f"Digite o elemento {i+1} da lista: "))
        lista.append(numero)
    return lista

def buscar_elemento(lista, elemento):
    for i, num in enumerate(lista):
        if num == elemento:
            return i
    return -1



if __name__ == "__main__":
    main()                