class Calculadora():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Operacoes(Calculadora):
    def soma(self, a, b):
        super().__init__(a, b)
        c = a+b
        return c

    def sub(self, a, b):
        super().__init__(a, b)
        return a-b

    def mult(self, a, b):
        super().__init__(a, b)
        return a*b

    def div(self, a, b):
        super().__init__(a, b)
        return a/b
