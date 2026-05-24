# 01-scripts/04-plot-methods.py

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from mma_project.data.loader import get_engine, load_sql

def main():
    print("🎨 Generando visualización de métodos de victoria...")
    
    # 1. Extracción (ELT)
    engine = get_engine()
    query = load_sql('get_victory_methods.sql')
    
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        
    # Estandarizamos columnas a minúsculas para evitar errores
    df.columns = df.columns.str.lower()
    
    # 2. Transformación (Pivot y Porcentajes)
    pivot_df = df.pivot(index='weight_class', columns='victory_method', values='total').fillna(0)
    pivot_df_pct = pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100
    
    # Ordenamos de menor a mayor porcentaje de Nocauts para que la gráfica cuente una historia visual clara
    if 'Nocaut (KO/TKO)' in pivot_df_pct.columns:
        pivot_df_pct = pivot_df_pct.sort_values(by='Nocaut (KO/TKO)')

    # 3. Visualización con Matplotlib
    # Asignamos colores representativos
    colores = {
        'Decisión': '#3498db',      # Azul
        'Sumisión': '#2ecc71',      # Verde
        'Nocaut (KO/TKO)': '#e74c3c'  # Rojo
    }
    
    # Aseguramos el orden de los colores según las columnas disponibles
    colores_plot = [colores.get(col, '#95a5a6') for col in pivot_df_pct.columns]
    
    # Creamos la figura
    fig, ax = plt.subplots(figsize=(12, 8))
    pivot_df_pct.plot(kind='barh', stacked=True, color=colores_plot, ax=ax, edgecolor='white')
    
    # Formato y diseño
    plt.title('Probabilidad Empírica de Métodos de Victoria por Peso (UFC)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Porcentaje del Total de Peleas (%)', fontsize=12)
    plt.ylabel('Categoría de Peso', fontsize=12)
    plt.legend(title='Método de Victoria', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.xlim(0, 100)
    
    # Limpieza visual de los bordes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    
    # 4. Guardar en la carpeta de reportes
    # Subimos un nivel desde 01-scripts hasta la raíz, y entramos a 03-reports/figures/
    project_root = Path(__file__).parent.parent
    output_path = project_root / '03-reports' / 'figures' / 'metodos_victoria_por_peso.png'
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ ¡Gráfica generada y guardada con éxito en:\n {output_path}")

if __name__ == "__main__":
    main()