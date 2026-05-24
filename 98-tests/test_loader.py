# 98-tests/test_loader.py

import pytest
from sqlalchemy.engine.base import Engine
from mma_project.data.loader import get_engine, load_sql

def test_get_engine_crea_conexion():
    """Prueba que la función get_engine devuelva un motor válido de SQLAlchemy."""
    engine = get_engine()
    # Verificamos que el objeto sea del tipo correcto
    assert isinstance(engine, Engine), "El motor no se creó correctamente."

def test_load_sql_lee_archivo_existente():
    """Prueba que podamos cargar el script SQL que hicimos para la gráfica."""
    # Sabemos que 'get_victory_methods.sql' existe en 01-scripts/
    query = load_sql('get_victory_methods.sql')
    query_str = str(query).upper()
    
    # Si el archivo se leyó bien, el texto debe contener las palabras clave de SQL
    assert "SELECT" in query_str, "El archivo SQL parece estar vacío o mal leído."
    assert "FROM FIGHTS" in query_str, "No se está consultando la tabla correcta."

def test_load_sql_falla_con_archivo_falso():
    """Prueba que el sistema arroje un FileNotFoundError si el SQL no existe."""
    # pytest.raises verifica que el código "explote" intencionalmente con este error
    with pytest.raises(FileNotFoundError):
        load_sql('archivo_inventado_que_no_existe.sql')