#  Arquitectura del Ecosistema Analítico

Este documento explica cómo está construido nuestro proyecto y por qué elegimos estas herramientas. Utilizamos un modelo moderno llamado **ELT (Extract, Load, Transform)**.

## 1. Extracción (Extract)
Nuestros datos originales de la UFC en formato CSV se guardan en la carpeta `00-data/raw/`. Esta carpeta es sagrada; los datos ahí nunca se modifican a mano para no arruinar la información original.

## 2. Carga (Load)
En lugar de limpiar los datos con Pandas y gastar memoria en la computadora, cargamos los datos crudos directamente a una base de datos analítica súper rápida llamada **DuckDB** (`00-data/mma_database.duckdb`). 
Hacemos esto usando un script SQL (`02-insert-initial-data.sql`) que vacía la base y la vuelve a llenar, asegurando que nunca haya datos duplicados.

## 3. Transformación (Transform)
Toda la magia matemática pesada (como calcular las rachas de victorias o el diferencial de golpes de los peleadores) se la dejamos al motor de **DuckDB**. 
Nuestro código en Python (en la carpeta `src/`) solo funciona como un puente. Python manda la consulta SQL, DuckDB hace el cálculo pesado en milisegundos, y nos devuelve una tabla limpia lista para graficar o para entrenar modelos de Machine Learning.

##  Pruebas de Calidad
Para asegurar que nuestro código no se rompa si alguien del equipo modifica algo, implementamos pruebas automatizadas con `pytest` en la carpeta `98-tests/`.