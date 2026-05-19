from pathlib import Path
from sqlalchemy import text

# Apuntamos a la carpeta donde estarán los scripts DDL y DML
SQL_DIR = Path("01-scripts")

def load_sql(query_path: str) -> text:
    """Lee un archivo .sql y regresa el texto listo para SQLAlchemy
    
    Args:
        query_path: Nombre del archivo .sql (sin la extensión)
        
    Returns:
        Objeto TextClause con la consulta SQL.
    """
    full_path = SQL_DIR / f"{query_path}.sql"
    if not full_path.exists():
        raise FileNotFoundError(f"Archivo SQL no encontrado: {full_path}")
        
    return text(full_path.read_text())