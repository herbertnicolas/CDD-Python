from biblioteca import *

print("Bem-vindo à sua calculadora!")

while True:
    op = int(input("Qual a operação desejada? 1 = SOMA, 2 = SUBTRAÇAO, 3 = MULTIPLICAÇAO, 4 = DIVISAO , 5 = SAIR"))
    if op == 5:
        break

    n1 = float(input("Insira o primeiro numero"))
    n2 = float(input("Insira o segundo numero"))
    o = Operacoes(n1,n2)

    if op == 1:
        result = o.soma(n1,n2)
        print(result)
    elif op == 2:
        result = o.sub(n1,n2)
        print(result)
    elif op == 3:
        result = o.mult(n1,n2)
        print(result)
    elif op == 4:
        result = o.div(n1,n2)
        print(result)
