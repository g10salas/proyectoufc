# 🥊 Proyecto UFC: Análisis Estadístico de Métodos de Victoria

Bienvenido a **proyectoufc**, un proyecto de análisis de datos e ingeniería ELT (Extract, Load, Transform) diseñado para procesar el histórico de combates de la Ultimate Fighting Championship (UFC) y responder matemáticamente a preguntas clave sobre el rendimiento de los atletas según su división de peso.

## 🎯 Pregunta de Investigación

Este proyecto fue construido para dar respuesta estructurada a la siguiente pregunta detonadora:

> *"¿Cómo cambia la proporción de victorias por Nocaut (KO/TKO) frente a Sumisiones dependiendo de la categoría de peso, y qué división tiene el mayor porcentaje de peleas que llegan hasta la decisión de los jueces?"*

## 🛠️ Tecnologías y Arquitectura

Para evitar el procesamiento pesado en memoria, este proyecto utiliza un enfoque **ELT**:
* **DuckDB:** Motor analítico principal para la limpieza, cruce y cálculo de variables (como el diferencial de golpes y agrupación de métodos de victoria) usando SQL directamente sobre los archivos fuente.
* **Python (Pandas/Seaborn):** Utilizado exclusivamente para la orquestación, extracción final de reportes agregados y visualización de datos.
* **uv:** Gestor de paquetes ultrarrápido para garantizar un entorno reproducible.

## 📂 Estructura del Repositorio

El proyecto sigue una estructura profesional de ciencia de datos:

* `00-data/`: Contiene los datos crudos (`raw/`) y el reporte estadístico final generado (`processed/reporte_divisiones.csv`).
* `01-scripts/`: Consultas SQL y scripts de calidad de datos para inicializar el motor DuckDB.
* `02-docs/`: Documentación fundamental del proyecto.
  * `arquitectura.md`: Explicación del modelo ELT.
  * `diccionario_datos.md`: Metadatos de las variables analizadas.
  * `guia_instalacion.md`: Pasos para reproducir el entorno.
  * `images/`: Gráficas generadas para la presentación final.
* `src/mma_project/`: Módulo instalable de Python. Contiene `data/loader.py` para la resolución dinámica de rutas absolutas y conexión segura a la base de datos.
*
