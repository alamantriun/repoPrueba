#esto indica en las erencias que metodos se usan a pesar de que los metodos tengan los mismos nombres de diferentes objetos

class A:
    def metodo(self):
        print("Hablar de A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d = D()

d.metodo()
