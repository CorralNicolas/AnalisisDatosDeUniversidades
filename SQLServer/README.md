
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

<img width="2048" height="1336" alt="Grafico" src="https://github.com/user-attachments/assets/628d4dd8-bc66-4a60-9fe0-a36fd3e1d755" />


---

## 📋 Diccionario de Tablas

En este Excel se definieron los campos, tipos de datos y claves primarias/foráneas de cada tabla.

<img width="1090" height="823" alt="Tablas" src="https://github.com/user-attachments/assets/177162dd-4f13-4215-9b57-6888994579b7" />

---

## 📋 Dataset Completo

Vista general del dataset original utilizado para alimentar las tablas.

<img width="2048" height="1280" alt="Imagen uno" src="https://github.com/user-attachments/assets/f511404d-06a8-47f2-8344-0598757b9248" />


---

## 📋 Dataset Mas limpio

Despues de realizar algunas alteraciones en SQL

<img width="2048" height="1280" alt="Imagen 2" src="https://github.com/user-attachments/assets/b9c70037-5dfb-4fac-9b83-5a8129f72df9" />


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

