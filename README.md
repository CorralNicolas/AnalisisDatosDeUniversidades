# Analisis Datos De Universidades

Proyecto final del curso de Data Analytics de Coderhouse, realizado en equipo por **Nicolás Corral** y **Natalia Delgado**.

📅 **Fecha de entrega:** Noviembre 2022  

## 🧠 Objetivo

Analizar el ranking de las mejores universidades del mundo en los últimos 5 años para detectar factores asociados a su posicionamiento: cantidad de alumnos, tamaño institucional, ubicación geográfica y ratios académico/estudiante.

## 🧰 Herramientas utilizadas

- **Power BI** para el análisis y visualización de los datos.
- **SQL** para realizar consultas sobre las bases de datos.
- **Excel** para limpieza y transformación inicial de los datos.

## 📊 Visualización

El dashboard en Power BI incluye:

- Sumatoria de alumnos internacionales por región y año.
- Ratio promedio de alumnos por docente.
- Puntaje promedio por zona.
- Ranking mundial filtrable por país, universidad y año.
- Evolución de ratios y cantidades de estudiantes desde 2018 hasta 2022.

## 🔍 Variables analizadas

- Tamaño de universidad
- Zona geográfica
- Cantidad de personal y alumnos
- Año del ranking
- Puntaje y posición en ranking global

## 🧮 Fórmulas DAX destacadas

```DAX
Puesto Promedio Por Zona = 
CALCULATE(AVERAGE(Ranking[score]),Ranking[score]>0)

Ranking Oficial = 
AVERAGE(Ranking[rank_display])

Sumatoria de alumnos Internacionales = 
CALCULATE(SUM(Personal[international_students]))
