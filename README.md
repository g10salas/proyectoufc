# 🥊 Análisis de Métodos de Victoria en la UFC por División de Peso

Este repositorio contiene el análisis de datos completo para responder a la siguiente pregunta de investigación:
> **¿Cómo cambia la proporción de victorias por Nocaut (KO/TKO) frente a Sumisiones dependiendo de la categoría de peso, y qué división tiene el mayor porcentaje de peleas que llegan a la decisión de los jueces?**

---

## 🧠 1. Motivación de los Datos
La elección de este conjunto de datos nace del interés por entender analíticamente las dinámicas de las artes marciales mixtas (MMA). En la UFC, las características físicas cambian drásticamente entre divisiones. Se busca comprobar con rigor estadístico si el peso y el género influyen en la vía de finalización del combate; por ejemplo, comprobando si en las divisiones más pesadas predomina el poder de nocaut, mientras que en las categorías más ligeras hay un mayor índice de sumisiones o un desgaste que lleva la pelea hasta las tarjetas de los jueces.

## 🗂️ 2. Origen y Obtención de los Datos
Los datos históricos fueron recolectados e integrados en formato tabular (`.csv`), conformando un ecosistema de cuatro entidades principales: `events`, `fighters`, `fighters_stats` y `fights`. Estas tablas contienen el registro oficial detallado de las carteleras, características biométricas de los peleadores y las estadísticas golpe a golpe de cada combate. Los archivos originales se mantienen intactos en la carpeta `00-data/raw/` para asegurar que todo el análisis parte de una fuente verificable.

## ⚙️ 3. Transformaciones y Manipulación (Data Pipeline)
Para armar el conjunto de datos final y generar los cálculos, el equipo diseñó un *pipeline* automatizado utilizando **Python** y **DuckDB**. El proceso consistió en:

* **Exploración Inicial:** Documentada en la carpeta `99-notebooks`, donde se inspeccionaron los esquemas de las tablas y se evaluó la calidad inicial de las columnas.
* **Creación del Motor Analítico:** Se estructuró la base de datos relacional `mma_database.duckdb` mediante scripts SQL y Python (carpeta `01-scripts`), garantizando una ingesta de datos limpia.
* **Agrupación y Cálculos:** Se filtraron combates con resultados nulos (como los "No Contest") y se construyeron métricas agregadas por división de peso. Se agruparon los totales de KOs, Sumisiones y Decisiones para obtener sus respectivos porcentajes sobre el total de peleas de la división.
* **Control de Calidad:** Se integró un script específico para auditar la manipulación de los datos, documentando la limpieza final en la carpeta `03-reports/data_quality/`.

---

## 📂 Estructura del Repositorio

El proyecto está diseñado bajo buenas prácticas de ingeniería de datos para garantizar su total reproducibilidad:

* `00-data/`: Contiene los datos crudos (`raw/`) y el motor de base de datos DuckDB.
* `01-scripts/`: *Pipeline* de ejecución numerado para inicializar, cargar, analizar, graficar y auditar los datos.
* `02-docs/`: Documentación técnica, incluyendo el diccionario de datos y la guía de instalación.
* `03-reports/`: Resultados analíticos, reportes de calidad y visualizaciones gráficas.
* `99-notebooks/`: Cuaderno interactivo con la exploración inicial de las tablas.
* `pyproject.toml` / `uv.lock`: Archivos de configuración para el gestor de dependencias, asegurando que el entorno se replique sin errores de versiones.

## 🚀 Resultados y Conclusiones Visuales
El cruce de la información y la respuesta definitiva a la pregunta de investigación se generaron automáticamente tras el procesamiento de datos y se pueden consultar en la visualización final:
📊 `03-reports/figures/metodos_victoria_por_peso.png`
