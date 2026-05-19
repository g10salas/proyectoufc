import pandas as pd
from sqlalchemy import text, create_engine

class Database:
    """Administrador de base de datos DuckDB para el proyecto de MMA"""
    
    def __init__(self, db_path: str) -> None:
        """Conecta a la base de datos DuckDB
        
        Args:
            db_path: Ruta al archivo de la base de datos (ej. 00-data/mma_database.duckdb)
        """
        # Se utiliza duckdb-engine para que SQLAlchemy reconozca DuckDB
        self.engine = create_engine(f"duckdb:///{db_path}")
        
    def query(self, sql: str | text, params: dict | None = None) -> pd.DataFrame:
        """Ejecuta consultas SELECT y regresa un DataFrame
        
        Args:
            sql: Consulta SQL a ejecutar
            params: Diccionario con parámetros opcionales
            
        Returns:
            DataFrame de Pandas con los resultados de la pelea o estadísticas.
        """
        if params:
            df = pd.read_sql_query(sql, self.engine, params=params)
        else:
            df = pd.read_sql_query(sql, self.engine)
            
        return df