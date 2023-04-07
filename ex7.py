soma_salarios = 0
qntd_habitantes  = 0
soma_nrofilhos = 0
qntd_salariomenor1500 = 0

salario = float(input("Digite o salário do habitante: "))


while(salario > 0):
    soma_salarios+=salario
    qntd_habitantes+=1
    nro_filhos = int(input("Digite o número de filhos do habitante: "))
    soma_nrofilhos+=nro_filhos
    if(salario < 1500):
        qntd_salariomenor1500+=1
    if(qntd_habitantes==1):
        maior_salario = salario
    else:
        if(salario > maior_salario):
            maior_salario = salario

    salario = float(input("Digite o salário do habitante: "))

media_salario = soma_salarios / qntd_habitantes
media_nrofilhos = soma_nrofilhos /qntd_habitantes
percent_salariomenor1500 = (qntd_salariomenor1500 * 100) / qntd_habitantes

print(f"Media dos salarios: {media_salario:.2f}")
print(f"Media do nro de filhos: {media_nrofilhos:.2f}")
print(f"Maior salario: {maior_salario:.2f}")
print(f"Percentual de pessoas com salário menor que R$ 1500,00: {percent_salariomenor1500:.2f}")