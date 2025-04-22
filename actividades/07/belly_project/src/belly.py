# src/belly.py
from src.clock import get_current_time


class Belly:
    def __init__(self, clock_service=None):
        self._pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.clock_service = clock_service or get_current_time
        self.tiempo_inicial = self.clock_service()

    def reset(self):
        self._pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.tiempo_inicial = self.clock_service()

    def comer(self, pepinos, modo_estres=False):
        if pepinos < 0:
            raise ValueError("No se pueden comer cantidades negativas de pepinos")
        if pepinos > 100 and not modo_estres:
            raise ValueError("No se pueden comer más de 100 pepinos")

        print(f"He comido {pepinos} pepinos.")
        self._pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        TIEMPO_MINIMO_HORAS = 1.5
        PEPINOS_MINIMOS = 10
        suficiente_tiempo = self.tiempo_esperado >= TIEMPO_MINIMO_HORAS
        suficientes_pepinos = self._pepinos_comidos > PEPINOS_MINIMOS
        return suficiente_tiempo and suficientes_pepinos

    def pepinos_comidos(self):
        return self._pepinos_comidos

    def predecir_gruñido(self, tiempo_adicional):
        TIEMPO_MINIMO_HORAS = 1.5
        PEPINOS_MINIMOS = 10
        tiempo_futuro = self.tiempo_esperado + tiempo_adicional
        suficiente_tiempo = tiempo_futuro >= TIEMPO_MINIMO_HORAS
        suficientes_pepinos = self._pepinos_comidos > PEPINOS_MINIMOS
        return suficiente_tiempo and suficientes_pepinos

    def pepinos_restantes(self):
        PEPINO_MINIMOS = 10
        pepinos_restantes = PEPINO_MINIMOS - self._pepinos_comidos
        return pepinos_restantes if pepinos_restantes > 0 else 0

    def tiempo_transcurrido(self):
        segundos_transcurridos = self.clock_service() - self.tiempo_inicial
        return segundos_transcurridos / 3600.0
