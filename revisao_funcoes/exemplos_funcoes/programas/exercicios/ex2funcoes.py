def main():
    tamanho_lista = int(input("Digite o tamanho da lista: "))
    lista_numerica = ler_lista(tamanho_lista)
    maior, menor = encontrar_maior_menor(lista_numerica)
    
    print("Lista numérica:", lista_numerica)
    print("Maior elemento:", maior)
    print("Menor elemento:", menor)

def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = float(input(f"Digite o elemento {i+1} da lista: "))
        lista.append(numero)
    return lista

def encontrar_maior_menor(lista):
    maior = menor = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento
    return maior, menor

if __name__ == "__main__":
    main()
