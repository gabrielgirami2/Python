nome = "gabriel"

print(type(nome))
print(nome[5])
print(nome[0:6])

nome = "Gabriel"
sobrenome = "Girami"
nome_completo = nome + " " + sobrenome
print(nome_completo)

texto = "Prova hoje"
print(len(texto))

minusculo = texto.lower()
print(minusculo)

maiusculo = texto.upper()
print(maiusculo)

palavra = texto.split(" ")
print(texto)

nova_palavra = texto.replace("Prova","Fodeu")
print(nova_palavra)

frase = "Hoje é dia de prova"

tam = len(frase)

for i in range(tam):
    print(frase[i])

palavra ="Fiap" 
  
palavra_invertida = palavra[::-1]
print(palavra_invertida)