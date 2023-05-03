lista_media = []
qntd_maiorigualsete = 0
for i in range(10):
    check1 = float(input("Digite a nota do checkpoint1: "))
    check2 = float(input("Digite a nota do checkpoint2: "))
    check3 = float(input("Digite a nota do checkpoint3: "))
    media = (check1 + check2 + check3) / 3
    lista_media.append(media)

for i in range(10):
    if(lista_media[i] >= 7.0):
        qntd_maiorigualsete+=1   

print(lista_media)    
print(f"o numero de alunos com media maior ou igual a sete é: {qntd_maiorigualsete:}")