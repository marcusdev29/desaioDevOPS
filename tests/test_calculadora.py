# tests/test_calculadora.py
import pytest
from app.calculadora import Calculadora

def test_somar():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5
    assert calc.somar(-1, 5) == 4

def test_dividir():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(9, 3) == 3

def test_dividir_por_zero():
    calc = Calculadora()
    with pytest.raises(ValueError, match="Divisão por zero não é permitida!"):
        calc.dividir(10, 0)

@pytest.mark.parametrize("base, expoente, resultado_esperado", [
    (2, 3, 8),
    (5, 0, 1),
    (10, 1, 10),
    (3, 4, 81),
])
def test_potencia(base, expoente, resultado_esperado):
    calc = Calculadora()
    assert calc.potencia(base, expoente) == resultado_esperado
