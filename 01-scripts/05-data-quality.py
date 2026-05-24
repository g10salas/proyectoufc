# 01-scripts/05-data-quality.py

import pandas as pd
from pathlib import Path
from mma_project.data.loader import get_engine

def main():
    print("🔍 Conectando a DuckDB para generar el informe de calidad...")
    engine = get_engine()
    
    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM fights;", conn)
    
    # Preparamos la ruta de salida
    project_root = Path(__file__).parent.parent
    output_path = project_root / '03-reports' / 'data_quality' / 'informe_calidad_fights.md'
    
    print("📊 Calculando estadísticas y matrices...")
    
    # 1. Separamos variables numéricas para correlaciones
    df_numerico = df.select_dtypes(include=['number'])
    
    # Escribimos el reporte manualmente
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# 📊 Informe de Calidad de Datos (Data Quality Report)\n")
        f.write("--- \n\n")
        
        f.write("## 1. Valores Faltantes (Missing Values)\n")
        f.write("Conteo de nulos por columna:\n```text\n")
        f.write(df.isnull().sum().to_string())
        f.write("\n```\n\n")
        
        f.write("## 2. Estadísticas Descriptivas completas\n")
        f.write("Medias, desviaciones estándar, mínimos y percentiles:\n```text\n")
        f.write(df.describe().to_string())
        f.write("\n```\n\n")
        
        f.write("## 3. Matriz de Correlaciones\n")
        f.write("Identificación de variables altamente correlacionadas:\n```text\n")
        f.write(df_numerico.corr().to_string())
        f.write("\n```\n\n")
        
        f.write("## 4. Detección de Outliers y Recomendaciones\n")
        f.write("* **Valores Atípicos:** Se recomienda comparar los valores 'max' del cuadro descriptivo con el percentil 75% (75%). Si el salto es masivo, hay outliers severos.\n")
        f.write("* **Limpieza sugerida:** Imputar nulos en columnas categóricas como 'Method' y 'Weight_Class' o eliminar esos registros específicos antes de entrenar modelos.\n")

    print("-" * 60)
    print(f"✅ ¡Informe generado con éxito sin romper las dependencias!")
    print(f"📁 Ruta: {output_path}")

if __name__ == "__main__":
    main()