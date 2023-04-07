i = 0
somaidade = 0

qntd = int(input("Insira a quantidade de alunos: "))

while i < qntd:
        idade = int(input("Digite sua idade: "))
        somaidade+=idade
        i+=1

mediaIdade = somaidade / qntd

print(f"A media de idades dos alunos é:{mediaIdade} ")
