dentro_intervalo = 0
fora_intervalo = 0
    
for i in range(10):
    num=int(input("Digite um número: "))
    if (num >= 10 and num <= 20):
        dentro_intervalo+=1
    else:
        fora_intervalo+=1

print(f"Números dentro do intervalo: {dentro_intervalo}")
print(f"Números fora do intervalo: {fora_intervalo}")
