# 📊 Preprocesamiento en Excel

En esta etapa se realizó la **descarga, inspección y validación inicial de los datos crudos** que luego fueron utilizados en SQL Server y Power BI.

---

## 🗂️ Actividades realizadas

1. **Importación del dataset** original desde un archivo `.csv`.
2. **Exploración de columnas**: revisión de categorías, tipos de dato y formato.
3. **Detección de valores nulos o inconsistencias**.
4. **Normalización básica de columnas** (renombrar encabezados, eliminar espacios, etc.).
5. División de datos por pestañas según temática (`Universidades`, `Personal`, `Ranking`, etc.).

---

## 🧰 Herramientas utilizadas

- **Microsoft Excel**
- Funciones de filtrado, ordenamiento y formato de tabla
- Validación rápida de datos mediante:
  - Filtros por campos vacíos
  - Contar valores únicos
  - Chequeo de integridad entre pestañas

---

## 📎 Archivos incluidos

- [2023 QS World University Rankings.csv](https://github.com/user-attachments/files/21675627/2023.QS.World.University.Rankings.csv) versión descargada directamente de la fuente.

<img width="1919" height="1018" alt="Screenshot 2025-08-07 230136" src="https://github.com/user-attachments/assets/b8980693-a9a9-49bb-a360-8c1805ec48f2" />

  
- [Tablas Resultado.xlsx](https://github.com/user-attachments/files/21675635/Tablas.Resultado.xlsx) versión lista para importar a SQL Server, sin valores nulos críticos.

  <img width="1919" height="995" alt="Screenshot 2025-08-07 230120" src="https://github.com/user-attachments/assets/036fbeeb-6fa7-4621-9c16-f7b29cda5574" />


---

## ✅ Resultados

- Se verificó que **no había valores nulos** en campos clave como `student_faculty_ratio` y `international_students`.
- Se prepararon tablas para ser cargadas a SQL con los nombres y tipos de datos apropiados.

---

Esta etapa fue clave para asegurar la **calidad del análisis posterior** realizado en SQL y Power BI.
