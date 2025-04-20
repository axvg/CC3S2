# language: es

Característica: Característica del estómago

  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos # Esto es 1.5 horas, deberia grunir
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos" # 2.5 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar solo en segundos
    Dado que he comido 20 pepinos
    Cuando espero "5400 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Comer una cantidad fraccionaria mayor que el umbral
    Dado que he comido 10.5 pepinos
    Cuando espero 1.5 horas
    Entonces mi estómago debería gruñir

  @english
  Escenario: Esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir

  @english
  Escenario: Esperar usando minutos en inglés
    Dado que he comido 25 pepinos
    Cuando espero "ninety minutes"
    Entonces mi estómago debería gruñir

 @english
  Escenario: Esperar usando 'half an hour'
    Dado que he comido 25 pepinos
    Cuando espero "half an hour"
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero "un tiempo aleatorio entre 1 y 3 horas"
    Entonces mi estómago debería gruñir