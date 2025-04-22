import pytest
from src.belly import Belly
from unittest.mock import MagicMock


def test_belly_initialization():
    belly = Belly()
    assert belly.pepinos_comidos() == 0
    assert belly.tiempo_esperado == 0


def test_comer_pepinos():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos() == 15
    belly.comer(5)
    assert belly.pepinos_comidos() == 20


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
    assert belly.pepinos_comidos() == 20
    assert belly.tiempo_esperado == 2.0

    belly.reset()
    assert belly.pepinos_comidos() == 0
    assert belly.tiempo_esperado == 0


def test_esta_gruñendo_conditions():
    belly = Belly()

    # Caso 1: Sin suficientes pepinos, tiempo suficiente
    belly.reset()
    belly.comer(10)
    belly.esperar(2.0)
    assert not belly.esta_gruñendo()

    # Caso 2: Suficientes pepinos, tiempo insuficiente
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


def test_comer_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(10.5)
    assert belly.pepinos_comidos() == 10.5
    belly.comer(0.25)
    assert belly.pepinos_comidos() == 10.75


def test_comer_pepinos_negativos():
    belly = Belly()
    with pytest.raises(ValueError) as err:
        belly.comer(-5)
    assert "No se pueden comer cantidades negativas de pepinos" in str(err.value)


def test_esta_gruñendo_con_pepinos_fraccionarios():
    belly = Belly()

    # Caso 1: Justo por encima del umbral con fraccion
    belly.reset()
    belly.comer(10.1)
    belly.esperar(1.5)
    assert belly.esta_gruñendo()

    # Caso 2: Justo por debajo del umbral con fraccion
    belly.reset()
    belly.comer(9.9)
    belly.esperar(2.0)
    assert not belly.esta_gruñendo()


def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo()


def test_pepinos_comidos():
    belly = Belly()
    belly.comer(10)
    assert belly.pepinos_comidos() == 10
    belly.comer(5)
    assert belly.pepinos_comidos() == 15


def test_predecir_gruñido_futuro():
    belly = Belly()
    belly.comer(8)
    belly.esperar(0.5)
    assert not belly.esta_gruñendo()
    assert not belly.predecir_gruñido(1.0)

    belly.comer(3)
    assert belly.predecir_gruñido(1.0)
    assert not belly.esta_gruñendo()


def test_pepinos_restantes():
    belly = Belly()
    belly.comer(5)
    assert belly.pepinos_restantes() == 5
    belly.comer(3)
    assert belly.pepinos_restantes() == 2
    belly.comer(2)
    assert belly.pepinos_restantes() == 0


def test_tiempo_transcurrid_mock():
    mock_clock = MagicMock(return_value=7200)
    belly = Belly(clock_service=mock_clock)
    belly.tiempo_inicial = 0
    assert belly.tiempo_transcurrido() == 2.0
