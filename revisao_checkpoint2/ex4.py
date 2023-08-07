qntd = int(input("Digite a quantidade de números para uma média aritmética: "))
i = 0
medianum= 0
while i < qntd:
    num = float(input("Digite um número: "))
    medianum+=num
    i+=1

media_aritmetica = medianum / qntd 

print(f"A média aritmetica ds numeros é:{media_aritmetica}")