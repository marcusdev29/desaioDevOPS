# app/calculadora.pywfrrewsf

class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida!")
        return a / b

    def potencia(self, base, expoente):
        return base ** expoente
