# 01-scripts/03-analyze-methods.py

import pandas as pd
from mma_project.data.loader import get_engine, load_sql

def main():
    print("🥊 Extrayendo análisis de métodos de victoria desde DuckDB...")
    
    # 1. Obtenemos la conexión y la consulta SQL
    engine = get_engine()
    query = load_sql('get_victory_methods.sql')
    
    # 2. Ejecutamos la consulta y la cargamos directamente a Pandas
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    
    # ¡NUEVO! Forzamos todas las columnas a minúsculas para evitar KeyErrors
    df.columns = df.columns.str.lower()
    
    # 3. Pivotamos la tabla usando los nombres en minúsculas
    pivot_df = df.pivot(index='weight_class', columns='victory_method', values='total').fillna(0)
    
    # Calculamos porcentajes por fila para responder a la "probabilidad empírica"
    pivot_df_pct = pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100
    
    print("\n📊 Distribución de Métodos de Victoria por Peso (Cantidades Totales):")
    print("-" * 60)
    print(pivot_df.astype(int))
    
    print("\n📈 Probabilidad Empírica por Peso (%):")
    print("-" * 60)
    print(pivot_df_pct.round(2))

if __name__ == "__main__":
    main()