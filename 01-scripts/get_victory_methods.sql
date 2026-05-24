-- 01-scripts/get_victory_methods.sql
-- Calcula la distribución de métodos de victoria por categoría de peso

WITH method_counts AS (
    SELECT 
        Weight_Class,
        -- Usamos ILIKE para que no importe si dice "SUB", "Sub" o "sub"
        CASE 
            WHEN Method ILIKE '%KO%' THEN 'Nocaut (KO/TKO)'
            WHEN Method ILIKE '%SUB%' THEN 'Sumisión'
            WHEN Method ILIKE '%DEC%' OR Method ILIKE '%Decision%' THEN 'Decisión'
            ELSE 'Otro'
        END AS victory_method,
        COUNT(*) as total
    FROM fights
    WHERE Weight_Class IS NOT NULL 
      AND Method IS NOT NULL
      AND Weight_Class != 'Catch Weight'
    GROUP BY 1, 2
)
SELECT 
    Weight_Class,
    victory_method,
    total
FROM method_counts
WHERE victory_method != 'Otro'
ORDER BY Weight_Class, total DESC;