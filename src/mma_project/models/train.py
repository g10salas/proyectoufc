# src/mma_project/models/train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from mma_project.data.loader import get_engine

def prepare_data(engine):
    """Extrae las características calculadas de DuckDB para el modelado."""
    query = """
    WITH striking_perf AS (
        SELECT 
            fight_id,
            fighter_1,
            (str_1 - str_2) AS striking_diff_f1,
            CASE WHEN result_1 = 'W' THEN 1 ELSE 0 END as win_f1
        FROM fights
    ),
    f1_streaks AS (
        SELECT 
            fight_id,
            striking_diff_f1,
            win_f1,
            COALESCE(SUM(win_f1) OVER (
                PARTITION BY fighter_1 
                ORDER BY fight_id
                ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
            ), 0) as win_streak_f1
        FROM striking_perf
    )
    SELECT striking_diff_f1, win_streak_f1, win_f1
    FROM f1_streaks;
    """
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

def main():
    print("🤖 Iniciando el pipeline de modelado predictivo...")
    engine = get_engine()
    
    # 1. Extracción de variables calculadas directamente en DuckDB (ELT)
    df = prepare_data(engine)
    
    X = df[['striking_diff_f1', 'win_streak_f1']]
    y = df['win_f1']
    
    # 2. División de conjuntos (80% entrenamiento, 20% prueba)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"📈 Registros para entrenamiento: {X_train.shape[0]}")
    print(f"📈 Registros para evaluación: {X_test.shape[0]}")
    
    # 3. Ajuste del modelo de Regresión Logística (Baseline de Probabilidad)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # 4. Evaluación de métricas estadísticas de predicción
    y_pred = model.predict(X_test)
    print("\n🎯 Resultados en el conjunto de prueba:")
    print(f"Exactitud Global (Accuracy): {accuracy_score(y_test, y_pred):.4f}")
    print("\n📋 Reporte de Clasificación Completo:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()