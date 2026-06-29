"""
Trabajo Practico Integrador - Programacion I
Gestion de Datos de Paises en Python: filtros, ordenamientos y estadisticas
Estudiante: CORNAGLIA Pablo

Este programa permite administrar un dataset de paises almacenado en un archivo CSV.
El dataset base contiene las 48 selecciones participantes de la Copa Mundial de Futbol.

El archivo CSV utiliza solamente los cuatro campos solicitados por la consigna:
- nombre
- poblacion
- superficie
- continente

El sistema aplica listas, diccionarios, funciones, condicionales, ciclos, lectura y
escritura de archivos CSV, busquedas, filtros, ordenamientos, estadisticas basicas,
validaciones y manejo de errores.
"""

import csv
import os

# ==========================================================
# CONSTANTES DEL PROGRAMA
# ==========================================================

ARCHIVO_CSV = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]
ANCHO_INTERFAZ = 108

# Dataset inicial de respaldo.
# Se usa solamente si el archivo CSV no existe.
# Cada pais se representa mediante un diccionario.
# Se utilizan solamente los campos pedidos por la consigna.
PAISES_INICIALES = [
    {"nombre": "México", "poblacion": 129875529, "superficie": 1964375, "continente": "America"},
    {"nombre": "Sudáfrica", "poblacion": 59390000, "superficie": 1221037, "continente": "Africa"},
    {"nombre": "República de Corea", "poblacion": 51740000, "superficie": 100210, "continente": "Asia"},
    {"nombre": "Chequia", "poblacion": 10850000, "superficie": 78867, "continente": "Europa"},
    {"nombre": "Canadá", "poblacion": 40100000, "superficie": 9984670, "continente": "America"},
    {"nombre": "Bosnia y Herzegovina", "poblacion": 3230000, "superficie": 51197, "continente": "Europa"},
    {"nombre": "Catar", "poblacion": 2716000, "superficie": 11586, "continente": "Asia"},
    {"nombre": "Suiza", "poblacion": 8900000, "superficie": 41285, "continente": "Europa"},
    {"nombre": "Brasil", "poblacion": 213993437, "superficie": 8515767, "continente": "America"},
    {"nombre": "Marruecos", "poblacion": 37460000, "superficie": 446550, "continente": "Africa"},
    {"nombre": "Haití", "poblacion": 11500000, "superficie": 27750, "continente": "America"},
    {"nombre": "Escocia", "poblacion": 5540000, "superficie": 77933, "continente": "Europa"},
    {"nombre": "Estados Unidos", "poblacion": 340110988, "superficie": 9833517, "continente": "America"},
    {"nombre": "Paraguay", "poblacion": 6780744, "superficie": 406752, "continente": "America"},
    {"nombre": "Australia", "poblacion": 26700000, "superficie": 7692024, "continente": "Oceania"},
    {"nombre": "Turquía", "poblacion": 85300000, "superficie": 783562, "continente": "Asia"},
    {"nombre": "Alemania", "poblacion": 83149300, "superficie": 357022, "continente": "Europa"},
    {"nombre": "Curaçao", "poblacion": 155000, "superficie": 444, "continente": "America"},
    {"nombre": "Costa de Marfil", "poblacion": 29400000, "superficie": 322463, "continente": "Africa"},
    {"nombre": "Ecuador", "poblacion": 18190000, "superficie": 256370, "continente": "America"},
    {"nombre": "Suecia", "poblacion": 10500000, "superficie": 450295, "continente": "Europa"},
    {"nombre": "Países Bajos", "poblacion": 17900000, "superficie": 41543, "continente": "Europa"},
    {"nombre": "Japón", "poblacion": 125800000, "superficie": 377975, "continente": "Asia"},
    {"nombre": "Túnez", "poblacion": 12000000, "superficie": 163610, "continente": "Africa"},
    {"nombre": "Bélgica", "poblacion": 11800000, "superficie": 30528, "continente": "Europa"},
    {"nombre": "Egipto", "poblacion": 109300000, "superficie": 1002450, "continente": "Africa"},
    {"nombre": "Irán", "poblacion": 89100000, "superficie": 1648195, "continente": "Asia"},
    {"nombre": "Nueva Zelanda", "poblacion": 5223000, "superficie": 268021, "continente": "Oceania"},
    {"nombre": "España", "poblacion": 48590000, "superficie": 505990, "continente": "Europa"},
    {"nombre": "Cabo Verde", "poblacion": 593000, "superficie": 4033, "continente": "Africa"},
    {"nombre": "Arabia Saudita", "poblacion": 37100000, "superficie": 2149690, "continente": "Asia"},
    {"nombre": "Uruguay", "poblacion": 3473727, "superficie": 176215, "continente": "America"},
    {"nombre": "Francia", "poblacion": 68600000, "superficie": 551695, "continente": "Europa"},
    {"nombre": "Senegal", "poblacion": 18100000, "superficie": 196722, "continente": "Africa"},
    {"nombre": "Irak", "poblacion": 45500000, "superficie": 438317, "continente": "Asia"},
    {"nombre": "Noruega", "poblacion": 5560000, "superficie": 385207, "continente": "Europa"},
    {"nombre": "Argentina", "poblacion": 47000000, "superficie": 2780400, "continente": "America"},
    {"nombre": "Argelia", "poblacion": 45600000, "superficie": 2381741, "continente": "Africa"},
    {"nombre": "Austria", "poblacion": 9200000, "superficie": 83879, "continente": "Europa"},
    {"nombre": "Jordania", "poblacion": 11400000, "superficie": 89342, "continente": "Asia"},
    {"nombre": "Portugal", "poblacion": 10600000, "superficie": 92212, "continente": "Europa"},
    {"nombre": "República Democrática del Congo", "poblacion": 111000000, "superficie": 2344858, "continente": "Africa"},
    {"nombre": "Uzbekistán", "poblacion": 37500000, "superficie": 448978, "continente": "Asia"},
    {"nombre": "Colombia", "poblacion": 53300000, "superficie": 1141748, "continente": "America"},
    {"nombre": "Inglaterra", "poblacion": 57000000, "superficie": 130279, "continente": "Europa"},
    {"nombre": "Croacia", "poblacion": 3850000, "superficie": 56594, "continente": "Europa"},
    {"nombre": "Panamá", "poblacion": 4500000, "superficie": 75417, "continente": "America"},
    {"nombre": "Ghana", "poblacion": 34100000, "superficie": 238533, "continente": "Africa"},
]

# ==========================================================
# FUNCIONES GENERALES
# ==========================================================

def mostrar_linea():
    """Muestra una linea separadora principal para ordenar la salida por consola."""
    print("=" * ANCHO_INTERFAZ)


def mostrar_sublinea():
    """Muestra una linea secundaria para separar bloques internos."""
    print("-" * ANCHO_INTERFAZ)


def mostrar_titulo(titulo, icono="🌎"):
    """Muestra un titulo con formato visual uniforme."""
    print(" ")
    mostrar_linea()
    print(f"{icono} {titulo.upper()}")
    mostrar_linea()


def pausar():
    """Pausa la ejecucion hasta que el usuario presione Enter."""
    input("\n↩️  Presione Enter para continuar...")


def normalizar_texto(texto):
    """Elimina espacios innecesarios y convierte el texto a minusculas."""
    return texto.strip().lower()


def formatear_numero(numero):
    """Devuelve un numero con separador de miles usando punto."""
    return f"{numero:,}".replace(",", ".")


def capitalizar_texto(texto):
    """Devuelve el texto con formato prolijo para almacenarlo y mostrarlo.

    Respeta conectores como "de" e "y" para evitar resultados poco naturales,
    por ejemplo: "Republica De Corea".
    """
    conectores = {"de", "del", "la", "las", "los", "el", "y"}
    palabras = texto.strip().split()
    resultado = []

    for indice, palabra in enumerate(palabras):
        palabra_minuscula = palabra.lower()
        if indice > 0 and palabra_minuscula in conectores:
            resultado.append(palabra_minuscula)
        else:
            resultado.append(palabra_minuscula.capitalize())

    return " ".join(resultado)


def leer_texto_obligatorio(mensaje):
    """Solicita texto y no permite campos vacios ni valores solamente numericos."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("\n❌ Error: el campo no puede estar vacío.")
        elif texto.isdigit():
            print("\n❌ Error: el texto no puede estar formado solamente por números.")
        else:
            return texto


def leer_entero(mensaje, minimo=None):
    """Solicita un numero entero y valida que sea correcto."""
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
            if minimo is not None and numero < minimo:
                print(f"❌ Error: el valor debe ser mayor o igual a {minimo}.")
            else:
                return numero
        except ValueError:
            print("❌ Error: debe ingresar un número entero válido.")

# ==========================================================
# FUNCIONES PARA MANEJO DEL ARCHIVO CSV
# ==========================================================

def crear_csv_inicial(ruta_archivo):
    """Crea el archivo CSV inicial cuando no existe."""
    try:
        with open(ruta_archivo, mode="w", encoding="utf-8-sig", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(PAISES_INICIALES)
        print(f"📁 Se creó el archivo {ruta_archivo} con datos iniciales.")
    except OSError as error:
        print(f"❌ Error al crear el archivo CSV inicial: {error}")


def validar_encabezados_csv(encabezados):
    """Verifica que el CSV tenga exactamente los encabezados requeridos."""
    if encabezados is None:
        return False

    encabezados_normalizados = [normalizar_texto(campo) for campo in encabezados]
    return encabezados_normalizados == CAMPOS


def validar_registro(fila, numero_linea):
    """Valida una fila del CSV y la convierte en un diccionario usable."""
    try:
        nombre = fila["nombre"].strip()
        continente = fila["continente"].strip()
        poblacion = int(fila["poblacion"])
        superficie = int(fila["superficie"])

        if not nombre or not continente:
            raise ValueError("nombre o continente vacio")
        if poblacion < 0:
            raise ValueError("la poblacion no puede ser negativa")
        if superficie <= 0:
            raise ValueError("la superficie debe ser mayor a cero")

        return {
            "nombre": capitalizar_texto(nombre),
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": capitalizar_texto(continente),
        }
    except (ValueError, KeyError) as error:
        print(f"⚠️  Advertencia: se omitió la línea {numero_linea} del CSV por formato inválido: {error}")
        return None


def cargar_paises(ruta_archivo):
    """Carga los paises desde el CSV y devuelve una lista de diccionarios."""
    paises = []

    if not os.path.exists(ruta_archivo):
        crear_csv_inicial(ruta_archivo)

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            if not validar_encabezados_csv(lector.fieldnames):
                print("❌ Error: el CSV no tiene los encabezados requeridos por la consigna.")
                print(f"ℹ️  Encabezados requeridos: {', '.join(CAMPOS)}")
                return paises

            for numero_linea, fila in enumerate(lector, start=2):
                registro = validar_registro(fila, numero_linea)
                if registro is not None:
                    paises.append(registro)
    except OSError as error:
        print(f"\n❌ Error al leer el archivo CSV: {error}")

    return paises


def guardar_paises(ruta_archivo, paises):
    """Guarda la lista de paises en el CSV."""
    try:
        with open(ruta_archivo, mode="w", encoding="utf-8-sig", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
        print("\n✅ Datos guardados correctamente en el archivo CSV.")
    except OSError as error:
        print(f"\n❌ Error al guardar el archivo CSV: {error}")

# ==========================================================
# FUNCIONES PARA MOSTRAR DATOS
# ==========================================================

def mostrar_pais(pais):
    """Muestra un pais de forma individual."""
    print(f"🌎 Nombre: {pais['nombre']}")
    print(f"👥 Población: {formatear_numero(pais['poblacion'])}")
    print(f"📐 Superficie: {formatear_numero(pais['superficie'])} km²")
    print(f"🌐 Continente: {pais['continente']}")


def mostrar_lista_paises(paises):
    """Muestra una lista de paises en formato de tabla."""
    if not paises:
        print("\n⚠️  No hay países para mostrar.")
        return

    ancho_nro = 4
    ancho_nombre = 40
    ancho_poblacion = 15
    ancho_superficie = 18
    ancho_continente = 15

    linea = (
        "+"
        + "-" * (ancho_nro + 2)
        + "+"
        + "-" * (ancho_nombre + 2)
        + "+"
        + "-" * (ancho_poblacion + 2)
        + "+"
        + "-" * (ancho_superficie + 2)
        + "+"
        + "-" * (ancho_continente + 2)
        + "+"
    )

    encabezado = (
        f"| {'N°':<{ancho_nro}} "
        f"| {'NOMBRE':<{ancho_nombre}} "
        f"| {'POBLACIÓN':>{ancho_poblacion}} "
        f"| {'SUPERFICIE':>{ancho_superficie}} "
        f"| {'CONTINENTE':>{ancho_continente}} |"
    )

    print(linea)
    print(encabezado)
    print(linea)

    for indice, pais in enumerate(paises, start=1):
        fila = (
            f"| {indice:<{ancho_nro}} "
            f"| {pais['nombre']:<{ancho_nombre}} "
            f"| {formatear_numero(pais['poblacion']):>{ancho_poblacion}} "
            f"| {formatear_numero(pais['superficie']):>{ancho_superficie}} "
            f"| {pais['continente']:>{ancho_continente}} |"
        )
        print(fila)

    print(linea)
    print()
    print("═" * len(linea))
    print(f"📌 TOTAL DE REGISTROS MOSTRADOS: {len(paises)}")
    print("═" * len(linea))

# ==========================================================
# FUNCIONES DE BUSQUEDA Y VALIDACION
# ==========================================================

def existe_pais(paises, nombre):
    """Verifica si ya existe un pais con el mismo nombre."""
    nombre_normalizado = normalizar_texto(nombre)
    return any(normalizar_texto(pais["nombre"]) == nombre_normalizado for pais in paises)


def buscar_paises_por_nombre(paises, termino):
    """Busca paises por coincidencia parcial o exacta."""
    termino_normalizado = normalizar_texto(termino)
    return [pais for pais in paises if termino_normalizado in normalizar_texto(pais["nombre"])]


def seleccionar_pais_de_resultados(resultados):
    """Permite seleccionar un pais cuando hay varias coincidencias."""
    mostrar_lista_paises(resultados)
    seleccion = leer_entero("👉 Seleccione el número del país: ", minimo=1)
    if seleccion > len(resultados):
        print("\n❌ Error: selección fuera de rango.")
        return None
    return resultados[seleccion - 1]

# ==========================================================
# FUNCIONES PRINCIPALES DEL SISTEMA
# ==========================================================

def agregar_pais(paises):
    """Agrega un nuevo pais validando todos los datos necesarios."""
    mostrar_titulo("AGREGAR PAÍS", "➕")

    nombre = capitalizar_texto(leer_texto_obligatorio("Nombre del país: "))
    if existe_pais(paises, nombre):
        print("\n❌ Error: ya existe un país registrado con ese nombre.")
        return

    poblacion = leer_entero("Población: ", minimo=0)
    superficie = leer_entero("Superficie en km²: ", minimo=1)
    continente = capitalizar_texto(leer_texto_obligatorio("Continente: "))

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    })
    guardar_paises(ARCHIVO_CSV, paises)
    print("✅ País agregado correctamente.")


def buscar_pais(paises):
    """Busca paises por nombre y muestra las coincidencias."""
    mostrar_titulo("BUSCAR PAÍS", "🔍")
    termino = leer_texto_obligatorio("Ingrese nombre o parte del nombre: ")
    resultados = buscar_paises_por_nombre(paises, termino)

    if resultados:
        print("\nResultados encontrados:")
        mostrar_lista_paises(resultados)
    else:
        print("\n⚠️  No se encontraron países que coincidan con la búsqueda.")


def actualizar_pais(paises):
    """Actualiza poblacion y superficie de un pais."""
    mostrar_titulo("ACTUALIZAR PAÍS", "✏️")
    termino = leer_texto_obligatorio("Ingrese el nombre o parte del nombre del país a actualizar: ")
    resultados = buscar_paises_por_nombre(paises, termino)

    if not resultados:
        print("\n⚠️  No se encontraron países para actualizar.")
        return

    if len(resultados) == 1:
        pais = resultados[0]
    else:
        print("ℹ️  Se encontraron varias coincidencias:")
        pais = seleccionar_pais_de_resultados(resultados)
        if pais is None:
            return

    print("\nRegistro actual:\n")
    mostrar_pais(pais)
    print("\nIngrese un valor numérico, sin puntos ni espacios.\n")
    pais["poblacion"] = leer_entero("Nueva población: ", minimo=0)
    pais["superficie"] = leer_entero("Nueva superficie en km²: ", minimo=1)
    guardar_paises(ARCHIVO_CSV, paises)
    print("✅ País actualizado correctamente.")


def eliminar_pais(paises):
    """Elimina un pais del dataset."""
    mostrar_titulo("ELIMINAR PAÍS", "🗑️")
    termino = leer_texto_obligatorio("Ingrese el nombre o parte del nombre del país a eliminar: ")
    resultados = buscar_paises_por_nombre(paises, termino)

    if not resultados:
        print("\n⚠️  No se encontraron países para eliminar.")
        return

    if len(resultados) == 1:
        pais = resultados[0]
    else:
        print("ℹ️  Se encontraron varias coincidencias:")
        pais = seleccionar_pais_de_resultados(resultados)
        if pais is None:
            return

    print("\nPaís seleccionado:\n")
    mostrar_pais(pais)
    confirmacion = input("\nConfirma que desea eliminar este país? (s/n): ").strip().lower()

    if confirmacion == "s":
        paises.remove(pais)
        guardar_paises(ARCHIVO_CSV, paises)
        print("✅  País eliminado correctamente.")
    else:
        print("↩️  Operación cancelada. Volviendo al menú principal...")

# ==========================================================
# FUNCIONES DE FILTRADO
# ==========================================================

def filtrar_por_continente(paises):
    """Filtra paises por continente."""
    mostrar_titulo("FILTRAR POR CONTINENTE", "🌐")
    continente = leer_texto_obligatorio("Ingrese continente: ")
    resultados = [pais for pais in paises if normalizar_texto(pais["continente"]) == normalizar_texto(continente)]

    if resultados:
        mostrar_lista_paises(resultados)
    else:
        print("\n⚠️  No se encontraron países para ese continente.")


def filtrar_por_rango(paises, campo, titulo):
    """Filtra paises por rango numerico de poblacion o superficie."""
    mostrar_titulo(titulo, "🔎")
    print("\nIngrese un valor numérico sin puntos ni espacios.\n")
    minimo = leer_entero("Valor mínimo: ", minimo=0)
    maximo = leer_entero("Valor máximo: ", minimo=0)

    if minimo > maximo:
        print("\n❌ Error: el valor mínimo no puede ser mayor que el valor máximo.")
        return

    resultados = [pais for pais in paises if minimo <= pais[campo] <= maximo]
    if resultados:
        mostrar_lista_paises(resultados)
    else:
        print("\n⚠️  No se encontraron países dentro del rango indicado.")


def menu_filtros(paises):
    """Submenu para opciones de filtrado."""
    while True:
        mostrar_titulo("MENÚ DE FILTROS", "🔎")
        print("1️⃣  Filtrar por continente")
        print("2️⃣  Filtrar por rango de población")
        print("3️⃣  Filtrar por rango de superficie")
        print("0️⃣  Volver al menú principal")
        opcion = input("👉 Seleccione una opción: ").strip()

        if opcion == "1":
            filtrar_por_continente(paises)
            pausar()
        elif opcion == "2":
            filtrar_por_rango(paises, "poblacion", "FILTRAR POR RANGO DE POBLACIÓN")
            pausar()
        elif opcion == "3":
            filtrar_por_rango(paises, "superficie", "FILTRAR POR RANGO DE SUPERFICIE")
            pausar()
        elif opcion == "0":
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")

# ==========================================================
# FUNCIONES DE ORDENAMIENTO
# ==========================================================

def ordenar_paises(paises, campo, descendente=False):
    """Devuelve una copia ordenada de la lista de paises."""
    if campo in ["nombre", "continente"]:
        return sorted(paises, key=lambda pais: normalizar_texto(pais[campo]), reverse=descendente)
    return sorted(paises, key=lambda pais: pais[campo], reverse=descendente)


def menu_ordenamientos(paises):
    """Submenu para ordenar paises por distintos criterios."""
    while True:
        mostrar_titulo("MENÚ DE ORDENAMIENTOS", "📋")
        print("1️⃣  Ordenar por nombre ascendente")
        print("2️⃣  Ordenar por nombre descendente")
        print("3️⃣  Ordenar por población ascendente")
        print("4️⃣  Ordenar por población descendente")
        print("5️⃣  Ordenar por superficie ascendente")
        print("6️⃣  Ordenar por superficie descendente")
        print("0️⃣  Volver al menú principal")
        opcion = input("👉 Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_lista_paises(ordenar_paises(paises, "nombre"))
            pausar()
        elif opcion == "2":
            mostrar_lista_paises(ordenar_paises(paises, "nombre", True))
            pausar()
        elif opcion == "3":
            mostrar_lista_paises(ordenar_paises(paises, "poblacion"))
            pausar()
        elif opcion == "4":
            mostrar_lista_paises(ordenar_paises(paises, "poblacion", True))
            pausar()
        elif opcion == "5":
            mostrar_lista_paises(ordenar_paises(paises, "superficie"))
            pausar()
        elif opcion == "6":
            mostrar_lista_paises(ordenar_paises(paises, "superficie", True))
            pausar()
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

# ==========================================================
# FUNCIONES DE ESTADISTICAS
# ==========================================================

def calcular_cantidad_por_continente(paises):
    """Calcula la cantidad de paises por continente."""
    conteo = {}
    for pais in paises:
        continente = pais["continente"]
        conteo[continente] = conteo.get(continente, 0) + 1
    return conteo


def mostrar_estadisticas(paises):
    """Muestra estadisticas generales del dataset."""
    mostrar_titulo("ESTADÍSTICAS GENERALES", "📊")

    if not paises:
        print("\n⚠️  No hay datos suficientes para calcular estadísticas.")
        return

    pais_mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])
    promedio_poblacion = sum(pais["poblacion"] for pais in paises) / len(paises)
    promedio_superficie = sum(pais["superficie"] for pais in paises) / len(paises)
    cantidad_por_continente = calcular_cantidad_por_continente(paises)

    print("\n🏆 PAÍS CON MAYOR POBLACIÓN:\n")
    mostrar_pais(pais_mayor_poblacion)
    print(" ")
    mostrar_linea()
    print("\n📉 PAÍS CON MENOR POBLACIÓN:\n")
    mostrar_pais(pais_menor_poblacion)
    print(" ")
    mostrar_linea()
    print("\n📊 PROMEDIOS:\n")
    print(f"👥 PROMEDIO DE POBLACIÓN: {formatear_numero(round(promedio_poblacion))}")
    print(f"📐 PROMEDIO DE SUPERFICIE: {formatear_numero(round(promedio_superficie))} km²")
    print(" ")
    mostrar_linea()
    print("\n🌐 CANTIDAD DE PAÍSES POR CONTINENTE:\n")
    for continente, cantidad in sorted(cantidad_por_continente.items()):
        print(f"🔵 {continente}: {cantidad}")

# ==========================================================
# MENU PRINCIPAL
# ==========================================================

def mostrar_menu_principal():
    """Muestra el menu principal del sistema."""
    print()
    mostrar_linea()
    print("        🌎 SISTEMA DE GESTIÓN DE DATOS - MUNDIAL DE FÚTBOL 2026 🌎")
    print("                    EE.UU • MÉXICO • CANADÁ")
    mostrar_linea()
    print("\nBienvenido al sistema de gestión de datos de los países que integran el Mundial.\nPara realizar una acción, elija una de las opciones del menú principal:\n ")
    
    print("1️⃣  MOSTRAR TODOS LOS PAÍSES")
    print("2️⃣  AGREGAR PAÍS")
    print("3️⃣  ACTUALIZAR POBLACIÓN Y SUPERFICIE DE UN PAÍS")
    print("4️⃣  BUSCAR PAÍS")
    print("5️⃣  FILTRAR PAÍSES")
    print("6️⃣  ORDENAR PAÍSES")
    print("7️⃣  MOSTRAR ESTADÍSTICAS")
    print("8️⃣  ELIMINAR PAÍS")
    print("0️⃣  SALIR DEL SISTEMA")


def main():
    """Funcion principal del programa."""
    paises = cargar_paises(ARCHIVO_CSV)
    print(f"✅ Se cargaron {len(paises)} países desde el archivo CSV.")

    while True:
        mostrar_menu_principal()
        opcion = input("👉 Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_titulo("LISTADO DE PAÍSES", "📋")
            mostrar_lista_paises(paises)
            pausar()
        elif opcion == "2":
            agregar_pais(paises)
            pausar()
        elif opcion == "3":
            actualizar_pais(paises)
            pausar()
        elif opcion == "4":
            buscar_pais(paises)
            pausar()
        elif opcion == "5":
            menu_filtros(paises)
        elif opcion == "6":
            menu_ordenamientos(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
            pausar()
        elif opcion == "8":
            eliminar_pais(paises)
            pausar()
        elif opcion == "0":
            guardar_paises(ARCHIVO_CSV, paises)
            print("\n✅ Programa finalizado correctamente.")
            print("👋 ¡Gracias por utilizar el Sistema de Gestión de Datos de Países!")
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")

# ==========================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":
    main()
