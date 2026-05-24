-- =====================================================================
-- 📜 01-scripts/02-insert-initial-data.sql
-- 🥊 Ingesta masiva de datos históricos reales de la UFC a DuckDB
-- =====================================================================

-- 1. Limpieza preventiva de tablas (Evita Constraint Errors de llaves duplicadas)
-- Se eliminan en orden inverso a sus dependencias para no romper restricciones
DELETE FROM fights;
DELETE FROM fighters_stats;
DELETE FROM fighters;
DELETE FROM events;

-- 2. Carga de Entidades Base (Tablas independientes)
-- Cargamos primero los catálogos de peleadores y eventos históricos
COPY fighters FROM '00-data/raw/fighters.csv' (HEADER TRUE, DELIMITER ',');
COPY events FROM '00-data/raw/events.csv' (HEADER TRUE, DELIMITER ',');

-- 3. Carga de Entidades Métricas (Tablas dependientes)
-- Finalmente inyectamos las estadísticas detalladas y el histórico de combates
COPY fighters_stats FROM '00-data/raw/fighters_stats.csv' (HEADER TRUE, DELIMITER ',');
COPY fights FROM '00-data/raw/fights.csv' (HEADER TRUE, DELIMITER ',');