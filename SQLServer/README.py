
# 🏫 Análisis del Ranking de Universidades del Mundo

Proyecto final del curso de Data Analytics en **Coderhouse**, realizado por **Nicolás Corral** y **Natalia Delgado**.

📅 **Fecha:** Noviembre 2022  
👨‍🏫 **Profesora:** Rebeca Figueroa | **Tutor:** Ismael Eiroa

---

## 🎯 Objetivo del Proyecto

Analizar el ranking de las mejores universidades del mundo en los últimos 5 años, buscando patrones y relaciones entre variables como:

- Cantidad de estudiantes internacionales
- Tamaño de las universidades
- Staff académico
- Zona geográfica

---

## 🛠️ Herramientas Utilizadas

- **Power BI**: Visualización de datos e informes interactivos
- **SQL**: Modelado de datos y consultas relacionales
- **Excel**: Limpieza y preparación de los datasets

---

## 🧱 Modelo de Datos

Se diseñó un modelo relacional compuesto por las siguientes tablas principales:

- `Universidades`
- `Ranking`
- `Personal`
- `Localización`
- `Tamaño`
- `Calendario`
- `Año`

🔗 Ver imagen del modelo entidad-relación en la carpeta `/assets` (o `/informe` si preferís unificar).

---

## 🧮 Fórmulas DAX destacadas en Power BI

```DAX
Puesto Promedio Por Zona = 
CALCULATE(AVERAGE(Ranking[score]),Ranking[score]>0)

Ranking Oficial = 
AVERAGE(Ranking[rank_display])

Sumatoria de alumnos Internacionales = 
CALCULATE(SUM(Personal[international_students]))
```

---

## 📊 Visualizaciones del Dashboard

- Sumatoria de alumnos internacionales por zona, país y año
- Ratio promedio alumnos/docente por año y por tamaño institucional
- Puntaje promedio por zona
- Ranking mundial top 20 según filtros
- Evolución histórica desde 2018 a 2022

---

## 📂 Estructura del Repositorio

```
📁 universidades-ranking/
├── README.md
├── sql/
│   └── consultas_creacion_y_exploracion.sql
├── informe/
│   └── informe_final.pdf
│   └── modelo_entidad_relacion.png
├── dashboard/
│   └── universidades.pbix
├── data/
│   └── dataset_muestra.xlsx
```

---

## 🧠 Conclusiones del Análisis

- Las universidades mejor rankeadas suelen tener **una baja relación estudiantes/docente**.
- Existen **diferencias notorias por región geográfica**.
- La **cantidad de estudiantes internacionales** también tiene una correlación moderada con la calidad del ranking.

---

## 🔮 Posibles Extensiones Futuras

- Incluir variable de **estudiantes becados** para analizar oportunidades económicas.
- Agregar encuestas de satisfacción estudiantil.
- Evaluar cómo cambia el ranking con el paso del tiempo para cada universidad.

---

Este proyecto es parte de mi portfolio profesional. Si querés ver más, visitá mi [GitHub](https://github.com/tu-usuario) o conectá en [LinkedIn](https://linkedin.com/in/tu-perfil).
