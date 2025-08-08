
-- ==========================
-- CREACIÓN DE TABLAS (DDL)
-- ==========================

-- Tabla de Universidades
CREATE TABLE Universidades (
  IDUniversidades INT PRIMARY KEY,
  Nombre_Uni VARCHAR(50),
  Tipo VARCHAR(20),
  IDZona VARCHAR(20),
  IDTamaño VARCHAR(20)
);

-- Tabla de Localización
CREATE TABLE Localizacion (
  IDZona VARCHAR(50) PRIMARY KEY,
  Pais VARCHAR(50),
  Zona VARCHAR(50),
  Region VARCHAR(50)
);

-- Tabla de Tamaño
CREATE TABLE Tamaño (
  IDTamaño VARCHAR(20) PRIMARY KEY,
  Descrip_Tamaño VARCHAR(20)
);

-- Tabla Ranking
CREATE TABLE Ranking (
  IDRank_Año INT PRIMARY KEY,
  Año INT,
  IDUniversidades INT,
  Ranking INT,
  Puntaje INT
);

-- Tabla de Personal
CREATE TABLE Personal (
  IDPersonal VARCHAR(50) PRIMARY KEY,
  IDUniversidades INT,
  Año INT,
  Estudiantes_Int INT,
  Estudiantes_ratio FLOAT,
  Staff INT
);

-- Tabla Calendario
CREATE TABLE Calendario (
  Año INT PRIMARY KEY,
  Fecha DATE,
  Dia INT,
  Mes INT
);

-- ==========================
-- CONSULTAS DE EXPLORACIÓN
-- ==========================

-- Promedio de ranking por zona
SELECT L.Zona, AVG(R.Ranking) AS Promedio_Ranking
FROM Ranking R
JOIN Universidades U ON R.IDUniversidades = U.IDUniversidades
JOIN Localizacion L ON U.IDZona = L.IDZona
GROUP BY L.Zona;

-- Evolución del ratio de estudiantes por año
SELECT Año, AVG(Estudiantes_ratio) AS Ratio_Promedio
FROM Personal
GROUP BY Año
ORDER BY Año;

-- Top 10 universidades con más estudiantes internacionales
SELECT U.Nombre_Uni, SUM(P.Estudiantes_Int) AS Total_Internacionales
FROM Personal P
JOIN Universidades U ON P.IDUniversidades = U.IDUniversidades
GROUP BY U.Nombre_Uni
ORDER BY Total_Internacionales DESC
LIMIT 10;

-- ==========================
-- VISTA EJEMPLO
-- ==========================

CREATE VIEW RankingZona AS
SELECT L.Zona, U.Nombre_Uni, R.Año, R.Ranking, R.Puntaje
FROM Ranking R
JOIN Universidades U ON R.IDUniversidades = U.IDUniversidades
JOIN Localizacion L ON U.IDZona = L.IDZona;
