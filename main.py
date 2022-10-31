import biblioteca

print("Bem-vindo à sua calculadora!")

while True:
    op = int(input("Qual a operação desejada? 1 = SOMA, 2 = SUBTRAÇAO, 3 = MULTIPLICAÇAO, 4 = DIVISAO , 5 = SAIR"))
    if op == 5:
        break
    n1 = float(input("Insira o primeiro numero"))
    n2 = float(input("Insira o segundo numero"))

    if op == 1:
        result = biblioteca.soma(n1, n2)
        print(result)
    elif op == 2:
        result = biblioteca.sub(n1, n2)
        print(result)
    elif op == 3:
        result = biblioteca.mult(n1, n2)
        print(result)
    elif op == 4:
        result = biblioteca.div(n1, n2)
        print(result)
