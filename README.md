# Analisis Datos De Universidades

Proyecto final del curso de Data Analytics de Coderhouse, realizado en equipo por **Nicolás Corral**.

<img width="1404" height="726" alt="Screenshot 2025-08-07 221429" src="https://github.com/user-attachments/assets/281fa2f4-a302-46cf-ae93-11601acb47bc" />

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

  <img width="1162" height="628" alt="image" src="https://github.com/user-attachments/assets/169c76ed-c063-4e90-bf9f-5c4907570fb6" />
  <img width="1391" height="724" alt="image" src="https://github.com/user-attachments/assets/2f1cd205-b779-4338-aedf-3da8f207f0df" />



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
