# 📖 Diccionario de Datos - Proyecto UFC

Este documento detalla el esquema de las principales tablas almacenadas en la base de datos analítica DuckDB (`mma_database.duckdb`). Las variables están divididas por entidades lógicas según el diseño del ecosistema.

## 🥊 1. Tabla de Peleas (`fights`)
Almacena el registro histórico de cada combate y las métricas de rendimiento de ambos peleadores durante el enfrentamiento.

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `fight_id` | VARCHAR (PK) | Identificador único global de la pelea. |
| `event_id` | VARCHAR (FK) | Identificador único del evento al que pertenece la pelea. |
| `fighter_id_1` / `_2` | VARCHAR (FK) | Identificador único del Peleador 1 y Peleador 2 respectivamente. |
| `fighter_1` / `_2` | VARCHAR | Nombre completo del Peleador 1 y Peleador 2. |
| `result_1` / `_2` | VARCHAR | Resultado del combate para cada peleador (`W` = Ganador, `L` = Perdedor, `D` = Empate). |
| `kd_1` / `_2` | INTEGER | Número de knockdowns anotados por cada peleador. |
| `str_1` / `_2` | INTEGER | Número total de golpes significativos conectados. |
| `td_1` / `_2` | INTEGER | Número de derribos (take downs) efectivos logrados. |
| `sub_1` / `_2` | INTEGER | Número de intentos de sumisión ejecutados. |
| `sig_str_pct_1` / `_2` | FLOAT | Porcentaje de efectividad de golpes significativos lanzados. |
| `ctrl_1` / `_2` | FLOAT | Tiempo total de control posicional en el suelo o contra la reja (en segundos). |
| `weight_class` | VARCHAR | División o categoría de peso oficial en la que se pactó el combate. |
| `method` | VARCHAR | Método oficial de finalización del combate (`KO/TKO`, `Submission`, `Decision`). |
| `round_num` | INTEGER | Asalto final en el que terminó el combate. |
| `fight_time` | VARCHAR | Minuto exacto en el que el réferi detuvo las acciones en el asalto final. |

## 📈 2. Tabla de Estadísticas Acumuladas (`fighters_stats`)
Contiene el perfil histórico resumido y métricas de estilo consolidadas para cada atleta.

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `fighter_id` | VARCHAR (PK) | Identificador único global del peleador. |
| `full_name` | VARCHAR | Nombre completo registrado. |
| `ht` / `wt` | FLOAT / FLOAT | Estatura (Height) y peso (Weight) de referencia del atleta. |
| `stance` | VARCHAR | Postura de combate predominante (`Orthodox`, `Southpaw`, `Switch`). |
| `ko_rate` | FLOAT | Proporción histórica de victorias obtenidas por la vía del Nocaut. |
| `sub_rate` | FLOAT | Proporción histórica de victorias obtenidas por la vía de la Sumisión. |
| `dec_rate` | FLOAT | Proporción histórica de combates que se definieron por las tarjetas. |
| `fighting_style` | VARCHAR | Clasificación algorítmica del estilo de pelea (`Striker`, `Wrestler`, `Hybrid`). |