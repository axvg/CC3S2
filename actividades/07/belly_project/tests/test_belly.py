import pytest
from src.belly import Belly

def test_belly_initialization():
    belly = Belly()
    assert belly.pepinos_comidos == 0
    assert belly.tiempo_esperado == 0

def test_comer_pepinos():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15
    belly.comer(5)
    assert belly.pepinos_comidos == 20

def test_esperar_tiempo():
    belly = Belly()
    belly.esperar(1.0)
    assert belly.tiempo_esperado == 1.0
    belly.esperar(0.5)
    assert belly.tiempo_esperado == 1.5

def test_reset():
    belly = Belly()
    belly.comer(20)
    belly.esperar(2.0)
    assert belly.pepinos_comidos == 20
    assert belly.tiempo_esperado == 2.0

    belly.reset()
    assert belly.pepinos_comidos == 0
    assert belly.tiempo_esperado == 0

def test_esta_gruñendo_conditions():
    belly = Belly()

    # Caso 1: Sin suficientes pepinos, tiempo suficiente
    belly.reset()
    belly.comer(10)
    belly.esperar(2.0)
    assert not belly.esta_gruñendo()

    #Caso 2: Suficientes pepinos, tiempo insuficiente
    belly.reset()
    belly.comer(20)
    belly.esperar(1.0)
    assert not belly.esta_gruñendo()

    # Caso 3: Suficientes pepinos, tiempo justo
    belly.reset()
    belly.comer(20)
    belly.esperar(1.5)
    assert belly.esta_gruñendo()

    # Caso 4: Suficientes pepinos, tiempo excesivo
    belly.reset()
    belly.comer(20)
    belly.esperar(2.0)
    assert belly.esta_gruñendo()

    # Caso 5: Suficientes pepinos, tiempo acumulado
    belly.reset()
    belly.comer(20)
    belly.esperar(1.0)
    assert not belly.esta_gruñendo()
    belly.esperar(0.6)
    assert belly.esta_gruñendo()
