# 01-scripts/test_db.py

from mma_project.data.loader import get_engine
from sqlalchemy import text
import pandas as pd

def main():
    print("🥊 Conectando a la base de datos analítica DuckDB...")
    
    # Mandamos llamar el motor desde nuestro propio paquete
    engine = get_engine()
    
    # Diccionario con las consultas de conteo para cada tabla
    tablas = {
        "Eventos (events)": "SELECT COUNT(*) FROM events;",
        "Peleadores (fighters)": "SELECT COUNT(*) FROM fighters;",
        "Estadísticas (fighters_stats)": "SELECT COUNT(*) FROM fighters_stats;",
        "Peleas (fights)": "SELECT COUNT(*) FROM fights;"
    }
    
    print("\n📊 Resumen de Ingesta de Datos (ELT - Load):")
    print("-" * 40)
    
    # Abrimos la conexión y ejecutamos las consultas
    with engine.connect() as conn:
        for nombre, query in tablas.items():
            # .scalar() extrae directamente el valor numérico del COUNT
            total_registros = conn.execute(text(query)).scalar()
            print(f"✅ {nombre}: {total_registros} registros cargados.")
            
    print("-" * 40)
    print("🚀 ¡Conexión exitosa! El paquete mma_project está listo para analizar datos.")

if __name__ == "__main__":
    main()