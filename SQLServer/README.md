
# 🗃️ Proyecto SQL Server – Modelo Universidades

Este directorio contiene todo lo relacionado con el modelado relacional y las consultas SQL utilizadas en el análisis de datos del ranking de universidades.

## 📌 Objetivo

Diseñar una base de datos relacional para estructurar y analizar información de universidades del mundo, enfocándonos en:

- Su ubicación geográfica
- Cantidad de estudiantes y personal académico
- Rankings y puntajes internacionales
- Relación entre variables como tamaño institucional, zona y calidad educativa

Todo esto fue trabajado en **SQL Server**, con normalización de tablas y creación de relaciones entre entidades clave.

---

## 🧱 Modelo Entidad-Relación

A continuación se muestra el diagrama entidad-relación del proyecto, que representa cómo se conectan las diferentes tablas.

![Modelo ER](../informe/Grafico.png)

---

## 📋 Diccionario de Tablas

En este Excel se definieron los campos, tipos de datos y claves primarias/foráneas de cada tabla.

![Estructura de Tablas](../informe/Tablas.png)

---

## 📊 Datos de Ejemplo

Ejemplo de los datos cargados en la tabla `Personal`, incluyendo columnas como `student_faculty_ratio`, `international_students`, `faculty_count`, etc.

![Datos tabla Personal](../informe/Imagen%20uno.png)

---

## 📋 Dataset Completo

Vista general del dataset original utilizado para alimentar las tablas.

![Vista del Dataset](../informe/Imagen%202.png)

---

## 📂 Contenido de esta Carpeta

- `consultas_creacion_y_exploracion.sql`:  
  Contiene la creación de tablas, consultas exploratorias y una vista para combinar datos de ranking y localización.

---

## 💡 Consultas destacadas incluidas

- Promedio de ranking por zona
- Evolución del ratio estudiantes/docente por año
- Top 10 universidades con más estudiantes internacionales
- Vista combinada de zona, universidad y puntaje

---

## 🧠 Conclusión

El modelado de datos en SQL permitió organizar, consultar y visualizar la información de manera eficiente para luego integrarse con Power BI y generar reportes interactivos.

