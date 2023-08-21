lista_original = [234, 64, 13467, 45.89, 23]

lista_descontos = [0.3, 0.004, 0.5, 0.03, 0.8]

lista_precos_desc = list(map(lambda preco, desc : preco - (preco * desc), lista_original, lista_descontos))

for i in range(len(lista_precos_desc)):
    print(f"{lista_precos_desc[i]:.2f}")