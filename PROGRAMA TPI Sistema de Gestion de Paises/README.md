# Trabajo Práctico Integrador - Gestión de Datos de Países en Python

**Estudiante:** CORNAGLIA Pablo
**Materia:** Programación I  
**Tema:** Gestión de datos de países participantes del Mundial de Fútbol 2026

## Descripción

Este proyecto consiste en una aplicación de consola desarrollada en Python 3.x para administrar un dataset de países. El archivo base `paises.csv` contiene 48 registros correspondientes a selecciones participantes del Mundial de Fútbol 2026 e incluye únicamente los campos solicitados por la consigna:

- nombre
- población
- superficie
- continente

El programa permite leer datos desde un archivo CSV, realizar consultas, aplicar filtros, ordenar registros y generar estadísticas básicas.

## Funcionalidades

- Mostrar todos los países registrados.
- Agregar un país con validación de campos obligatorios.
- Actualizar población y superficie de un país.
- Buscar un país por nombre con coincidencia parcial o exacta.
- Filtrar países por continente.
- Filtrar países por rango de población.
- Filtrar países por rango de superficie.
- Ordenar países por nombre, población o superficie.
- Mostrar estadísticas generales.
- Eliminar un país.
- Guardar cambios en el archivo CSV.
- Salir del sistema desde el menú principal.

## Requisitos

- Python 3.x.
- No requiere librerías externas.

## Cómo ejecutar

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto.
3. Ejecutar:

```bash
python gestion_paises.py
```

Si el archivo `paises.csv` no existe, el programa lo crea automáticamente con los 48 registros iniciales.

## Estructura del proyecto

```text
PROGRAMA TPI Sistema de Gestion de Paises/
├── TPI Sistema de Gestión de Países.py
├── paises.csv
├── README.md
```

## Ejemplo de salida esperada

```text
| N°   | NOMBRE                                   |       POBLACIÓN |         SUPERFICIE |      CONTINENTE |
| 1    | México                                   |     129.875.529 |          1.964.375 |         America |
| 2    | Sudáfrica                                |      59.390.000 |          1.221.037 |          Africa |
```

## Validaciones implementadas

- No se permiten campos vacíos.
- No se permiten nombres formados solamente por números.
- La población debe ser un número entero mayor o igual a cero.
- La superficie debe ser un número entero mayor a cero.
- Se evita registrar países duplicados.
- Se controlan errores de formato del archivo CSV.
- Se muestran mensajes claros cuando no existen resultados en búsquedas o filtros.

## Participación

CORNAGLIA Pablo: desarrollo del programa, organización del dataset, validaciones, documentación y preparación de la entrega.

## Links de enlace

- Repositorio GitHub: https://github.com/pabloke1987-hash/TPI-Sistema-de-Gestion-de-Paises
- Video demostrativo: https://youtu.be/BntPv5HF-mg
