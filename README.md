# Proyecto Final: Análisis de Métodos de Victoria en la UFC

Este repositorio contiene la arquitectura de datos, los scripts de preprocesamiento y los módulos de conexión necesarios para reproducir el análisis estadístico sobre cómo las diferentes categorías de peso en la UFC impactan la probabilidad de victorias por KO/TKO frente a Sumisiones.

## 👥 Equipo de Trabajo (Manejo de Datos)
* Gilberto Salas Camarillo
* [Nombre del Integrante 2]
* [Nombre del Integrante 3]

## 🛠️ Requisitos Técnicos
El proyecto está diseñado para ejecutarse dentro de un entorno de **GitHub Codespaces**, garantizando la misma configuración para todos los colaboradores y eliminando errores de compatibilidad.
* **Motor de Base de Datos:** DuckDB (v0.10.0+)
* **Lenguaje:** Python 3.x
* **Librerías Principales:** Pandas, SQLAlchemy, DuckDB-Engine

## 📂 Estructura del Repositorio
Para garantizar la modularidad, el código está organizado de la siguiente manera:
* `00-data/raw/`: Datasets históricos en formato `.csv` (intocables, preservando su estado original).
* `01-scripts/`: Scripts `.sql` con instrucciones DDL (Creación de tablas) y DML (Ingesta masiva).
* `src/mma_project/db/`: Módulos de Python para la conexión a la base de datos mediante SQLAlchemy.
* `notebooks/`: Libretas de Jupyter para el análisis exploratorio y la visualización final de resultados.

## 🚀 Instrucciones de Reproducibilidad

Para reconstruir la base de datos relacional `mma_database.duckdb` desde cero, abre la terminal en la raíz del proyecto y sigue estos pasos en orden estricto:

**1. Inicializar el entorno de Python**
Asegúrate de tener instaladas las dependencias y el paquete del proyecto configurados en el archivo `pyproject.toml`:
```bash
pip install -e .
```

**2. Crear la Estructura de la Base de Datos (DDL)**
Ejecuta el script de inicialización para crear las tablas vacías (`Events`, `Fighters`, `Fighters_Stats`, `Fights`) con sus llaves primarias.
```bash
duckdb 00-data/mma_database.duckdb < 01-scripts/01-init-db.sql
```

**3. Ingesta Masiva de Datos (DML)**
Carga los datos crudos desde la carpeta `raw/` hacia las tablas utilizando el comando `COPY` de DuckDB para una lectura de alto rendimiento.
```bash
duckdb 00-data/mma_database.duckdb < 01-scripts/02-insert-initial-data.sql
```

## 📊 Verificación Rápida
Una vez ejecutados los scripts, puedes abrir la consola interactiva desde la terminal:
```bash
duckdb 00-data/mma_database.duckdb
```
Y verificar el total de combates registrados en la tabla de hechos con la siguiente consulta:
```sql
SELECT COUNT(*) AS total_peleas FROM Fights;
```