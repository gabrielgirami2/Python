lista_produtos = []
resp = 1

while (resp != 0):
    print("1 - Inserção do produto")
    print("2 - Alteração do produto")
    print("3 - Exclusão do produto")
    print("4 - Exibição dos produtos")
    opc = int(input("Digite a opção desejada (1-4): "))

    if (opc == 1):
        try:
            cod = int(input("Digite o código: "))
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            salario = float(input("Digite o salário: "))
        except ValueError:
            print("Digite um valor numérico")
        else: 
            func = {'Codigo':cod, 'Nome':nome, 'Idade':idade, 'Salario':salario}
            lista_funcionarios.append(func)
        finally:
            print("Operação finalizada")