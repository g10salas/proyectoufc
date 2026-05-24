from pathlib import Path
from sqlalchemy import text

SQL_DIR = Path(__file__).parent.parent.parent.parent / "01-scripts"

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
        
    # Agregamos encoding='utf-8' para evitar problemas con acentos y caracteres especiales
    return text(full_path.read_text(encoding='utf-8'))