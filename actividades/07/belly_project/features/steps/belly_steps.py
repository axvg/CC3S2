from behave import given, when, then
import re
import random


# Funcion para manejar rangos de tiempo
def generar_tiempo_aleatorio(min_val, max_val):
    tiempo = round(random.uniform(min_val, max_val), 2)
    print(f"Tiempo aleatorio generado: {tiempo} horas")
    return tiempo


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return float(palabra) if "." in palabra else int(palabra)
    except ValueError:
        numeros_es = {
            "cero": 0,
            "uno": 1,
            "una": 1,
            "dos": 2,
            "tres": 3,
            "cuatro": 4,
            "cinco": 5,
            "seis": 6,
            "siete": 7,
            "ocho": 8,
            "nueve": 9,
            "diez": 10,
            "once": 11,
            "doce": 12,
            "trece": 13,
            "catorce": 14,
            "quince": 15,
            "dieciséis": 16,
            "diecisiete": 17,
            "dieciocho": 18,
            "diecinueve": 19,
            "veinte": 20,
            "treinta": 30,
            "cuarenta": 40,
            "cincuenta": 50,
            "sesenta": 60,
            "setenta": 70,
            "ochenta": 80,
            "noventa": 90,
            "media": 0.5,
        }

        numeros_en = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
            "twenty": 20,
            "thirty": 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty": 80,
            "ninety": 90,
            "half": 0.5,
        }

        # Intenta primero en español luego en ingles
        valor = numeros_es.get(palabra.lower(), None)
        if valor is None:
            valor = numeros_en.get(palabra.lower(), 0)
        return valor


@given("que he comido {cukes} pepinos")
def step_given_eaten_cukes(context, cukes):
    try:
        if "," in cukes:
            cukes = cukes.replace(",", ".")
        cantidad = float(cukes)
        context.belly.comer(cantidad)
        context.error = None
    except ValueError as err:
        context.error = str(err)


@when("espero {time_description}")
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()

    random.seed(99)  # Seed fijo

    match_range = re.search(
        r"(?:entre|from|between)\s+(\d+|\w+)\s+(?:y|and|to)\s+(\d+|\w+)\s+(horas?|hours?|minutos?|minutes?|segundos?|seconds?)",
        time_description,
    )

    if match_range:
        min_val = convertir_palabra_a_numero(match_range.group(1))
        max_val = convertir_palabra_a_numero(match_range.group(2))
        unidad = match_range.group(3)

        if re.match(r"minutos?|minutes?", unidad):
            min_val /= 60
            max_val /= 60
        elif re.match(r"segundos?|seconds?", unidad):
            min_val /= 3600
            max_val /= 3600

        total_time_in_hours = generar_tiempo_aleatorio(min_val, max_val)
    else:
        time_description = re.sub(r"\s+and\s+|\s+y\s+|\s*,\s*", " ", time_description)
        time_description = time_description.strip()

        hours = 0
        minutes = 0
        seconds = 0

        match_h = re.search(r"(\d+|\w+)\s*(?:horas?|hours?|h)", time_description)
        if match_h:
            hours = convertir_palabra_a_numero(match_h.group(1))
            time_description = time_description.replace(match_h.group(0), "", 1).strip()

        match_m = re.search(
            r"(\d+|\w+)\s*(?:minutos?|minutes?|min|m)", time_description
        )
        if match_m:
            minutes = convertir_palabra_a_numero(match_m.group(1))
            time_description = time_description.replace(match_m.group(0), "", 1).strip()

        match_s = re.search(
            r"(\d+|\w+)\s*(?:segundos?|seconds?|sec|s)", time_description
        )
        if match_s:
            seconds = convertir_palabra_a_numero(match_s.group(1))
            time_description = time_description.replace(match_s.group(0), "", 1).strip()

        total_time_in_hours = hours + (minutes / 60.0) + (seconds / 3600.0)

    context.belly.esperar(total_time_in_hours)


@then("mi estómago debería gruñir")
def step_then_belly_should_growl(context):
    assert (
        context.belly.esta_gruñendo()
    ), "Se esperaba que el estómago gruñera, pero no lo hizo."


@then("mi estómago no debería gruñir")
def step_then_belly_should_not_growl(context):
    assert (
        not context.belly.esta_gruñendo()
    ), "Se esperaba que el estómago no gruñera, pero lo hizo."


@then("debería ocurrir un error de cantidad {tipo_error}")
def step_then_should_raise_error(context, tipo_error):
    assert context.error is not None, "Se esperaba un error, pero no ocurrio ninguno"

    if tipo_error == "negativa":
        assert (
            "cantidades negativas" in context.error
        ), f"Error incorrecto: {context.error}"
    elif tipo_error == "excesiva":
        assert (
            "más de 100 pepinos" in context.error
        ), f"Error incorrecto: {context.error}"
    else:
        assert False, f"Tipo de error desconocido: {tipo_error}"
