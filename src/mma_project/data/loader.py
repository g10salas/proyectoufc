from pathlib import Path
from sqlalchemy import create_engine, text

# Definimos la raíz del proyecto dinámicamente usando la ubicación de este archivo
# Sube 4 niveles: data -> mma_project -> src -> proyectoufc
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
SQL_DIR = PROJECT_ROOT / "01-scripts"
DB_PATH = PROJECT_ROOT / "00-data" / "mma_database.duckdb"

def get_engine():
    """
    Crea y retorna la conexión a la base de datos DuckDB.
    """
    # Usamos SQLAlchemy con el dialecto de DuckDB
    return create_engine(f"duckdb:///{DB_PATH}")

def load_sql(query_name: str) -> text:
    """
    Busca un archivo .sql en la carpeta de scripts, lo lee y lo prepara para SQLAlchemy.
    """
    # Validamos si el archivo tiene la extensión o se la agregamos
    if not query_name.endswith('.sql'):
        query_name += '.sql'
        
    full_path = SQL_DIR / query_name
    
    if not full_path.exists():
        raise FileNotFoundError(f"🚨 Archivo SQL no encontrado en: {full_path}")
        
    return text(full_path.read_text(encoding='utf-8'))