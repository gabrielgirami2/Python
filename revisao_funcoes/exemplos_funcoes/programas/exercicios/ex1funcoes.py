
def main():
    tamanho_lista = int(input("Digite o tamanho da lista: "))
    lista_numerica = ler_lista(tamanho_lista)
    print("Lista numérica: ", lista_numerica)



def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = float(input(f"Digite o elemento {i+1} da lista: "))
        lista.append(numero)
    return lista

if __name__ == "__main__":
    main()
