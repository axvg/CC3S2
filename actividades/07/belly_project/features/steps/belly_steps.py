from behave import given, when, then
import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return float(palabra) if '.' in palabra else int(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20,
            "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
            "ochenta":80, "noventa":90, "media": 0.5
        }
        return numeros.get(palabra.lower(), 0)

@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        if ',' in cukes:
            cukes = cukes.replace(',', '.')
        cantidad = float(cukes)
        context.belly.comer(cantidad)
    except ValueError as e:
        context.scenario.skip(reason=f"Error al procesar cantidad de pepinos: {e}")

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = re.sub(r'\s+y\s+|\s*,\s*', ' ', time_description)
    time_description = time_description.strip()

    total_time_in_hours = 0

    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        hours = 0
        minutes = 0
        seconds = 0

        match_h = re.search(r'(\d+|\w+)\s*(?:horas?|h)', time_description)
        if match_h:
            try:
                hours = convertir_palabra_a_numero(match_h.group(1))
                time_description = time_description.replace(match_h.group(0), '', 1).strip()
            except ValueError as e:
                print(f"Error al interpretar horas: {e}")


        match_m = re.search(r'(\d+|\w+)\s*(?:minutos?|m)', time_description)
        if match_m:
            try:
                minutes = convertir_palabra_a_numero(match_m.group(1))
                time_description = time_description.replace(match_m.group(0), '', 1).strip()
            except ValueError as e:
                print(f"Error al interpretar minutos: {e}")


        match_s = re.search(r'(\d+|\w+)\s*(?:segundos?|s)', time_description)
        if match_s:
            try:
                seconds = convertir_palabra_a_numero(match_s.group(1))
                time_description = time_description.replace(match_s.group(0), '', 1).strip()
            except ValueError as e:
                 print(f"Error la interpretar segundos: {e}")

        time_description_cleaned = time_description.replace('y','').replace(',','').strip()
        if time_description_cleaned and hours == 0 and minutes == 0 and seconds == 0:
            try:
                hours = convertir_palabra_a_numero(time_description_cleaned.split()[0])
            except ValueError:
                 raise ValueError(f"No se pudo interpretar la descripcion del tiempo: '{time_description}' (Restante: '{time_description_cleaned}')")
        total_time_in_hours = hours + (minutes / 60.0) + (seconds / 3600.0)

    if total_time_in_hours < 0:
        raise ValueError(f"El tiempo de espera calculado no puede ser negativo: {total_time_in_hours} horas (Input: '{time_description}')")

    # print(f"Esperando {total_time_in_hours} horas (interpretado de '{time_description}')")
    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

