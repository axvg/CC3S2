# language: es

Característica: Característica del estómago

  @spanish
  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos # Esto es 1.5 horas, deberia grunir
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos" # 2.5 horas
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer pepinos y esperar solo en segundos
    Dado que he comido 20 pepinos
    Cuando espero "5400 segundos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  @spanish
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

  @spanish @random
  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero "un tiempo aleatorio entre 1 y 3 horas"
    Entonces mi estómago debería gruñir

  @english @random
  Escenario: Comer pepinos y esperar un tiempo aleatorio in english
    Dado que he comido 25 pepinos
    Cuando espero "between 1 and 3 hours"
    Entonces mi estómago debería gruñir

  @validacion
  Escenario: Manejar una cantidad negativa de pepinos
    Dado que he comido -5 pepinos
    Entonces debería ocurrir un error de cantidad negativa

  @validacion
  Escenario: Manejar una cantidad excesiva de pepinos
    Dado que he comido 150 pepinos
    Entonces debería ocurrir un error de cantidad excesiva

  @estres
  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir

  Escenario: Manejar tiempos complejos esp
    Dado que he comido 50 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Manejar tiempos complejos eng
    Dado que he comido 100 pepinos
    Cuando espero "2 hours, 10 minutes and 59 seconds"
    Entonces mi estómago debería gruñir

  Escenario: Comer muchos pepinos y esperar el tiempo suficiente
    Dado que he comido 15 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @historia-usuario
  Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @historia-usuario
  Escenario: Comer pocos pepinos y no esperar suficiente tiempo
    Dado que he comido 5 pepinos
    Cuando espero 1 hora
    Entonces mi estómago no debería gruñir

  @historia-usuario
  Escenario: Comer justo en el limite de pepinos y esperar el tiempo minimo
    Dado que he comido 11 pepinos
    Cuando espero 1.5 horas
    Entonces mi estómago debería gruñir

  Escenario: Saber cuantos pepinos puedo comer antes de gruñir
    Dado que he comido 8 pepinos
    Cuando pregunto cuantos pepinos mas puedo comer
    Entonces me dice que puedo comer 2 pepinos mas

  Escenario: Verificar que el estómago gruñe tras comer suficientes pepinos y esperar
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Predecir si mi estomago gruñira en el futuro
    Dado que he comido 8 pepinos
    Y he esperado 0.5 horas
    Cuando pregunto si mi estomago gruñira si espero 1.0 hora mas
    Entonces deberia recibir una prediccion de que no gruñira

  @criterio_nuevo
  Escenario: Ver cuantos pepinos puedo comer cuando no he comido ninguno
    Dado que he comido 0 pepinos
    Cuando pregunto cuantos pepinos mas puedo comer
    Entonces me dice que puedo comer 10 pepinos mas

  @criterio_nuevo
  Escenario: Ver cuantos pepinos puedo comer cuando ya he comido algunos
    Dado que he comido 8 pepinos
    Cuando pregunto cuantos pepinos mas puedo comer
    Entonces me dice que puedo comer 2 pepinos mas

  @criterio_nuevo
  Escenario: Ver cuantos pepinos puedo comer cuando estoy justo en el límite
    Dado que he comido 10 pepinos
    Cuando pregunto cuantos pepinos mas puedo comer
    Entonces me dice que puedo comer 0 pepinos mas

  @mock_clock
  Escenario: Medir tiempo transcurrido con reloj simulado
    Dado que el reloj inicial marca 10000
    Cuando el reloj avanza a 12800
    Entonces el tiempo transcurrido debería ser 46.67 minutos