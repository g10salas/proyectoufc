# 🚀 Guía de Instalación y Configuración del Entorno

¡Bienvenido al proyecto **proyectoufc**! Para que todo el código analítico, los scripts de DuckDB y las pruebas unitarias funcionen perfectamente en tu computadora o Codespace sin romper dependencias, sigue este tutorial paso a paso.

## 🛠️ Requisitos Previos
Este proyecto utiliza **`uv`**, un gestor de paquetes de Python ultra rápido que reemplaza a `pip`. Si estás trabajando en GitHub Codespaces, ya viene preinstalado.

## 🏃‍♂️ Paso a Paso para Empezar

### 1. Clonar el repositorio y entrar a la carpeta
Si acabas de descargar el proyecto, asegúrate de estar parado en la raíz del espacio de trabajo:

```bash
cd /workspaces/proyectoufc
```

### 2. Crear y activar el entorno virtual
Creamos un entorno aislado para que las librerías del proyecto no se mezclen con las de tu sistema:

```bash
uv venv
source .venv/bin/activate
```
*(Nota: En Codespaces, el entorno virtual suele activarse de forma automática al abrir la terminal).*

### 3. La Regla de Oro: Instalación del Paquete Local
Para que Python reconozca nuestra estructura interna de carpetas (`src/mma_project`) como una librería nativa y cargue todas las dependencias, **DEBES** ejecutar el siguiente comando en la raíz del proyecto:

```bash
uv pip install -e .[dev]
```

### 4. Verificar que todo funcione (La Prueba de Fuego)
Para comprobar que tu entorno se configuró correctamente y que tienes acceso a la base de datos DuckDB, ejecuta las pruebas automatizadas:

```bash
pytest 98-tests/
```
Si la terminal pinta **3 passed** en color verde, ¡estás listo para programar!

---

## ⚠️ Regla Importante de Concurrencia (DuckDB)
DuckDB es una base de datos embebida muy rápida, pero tiene una restricción estricta: **Solo un proceso puede escribir o leer el archivo a la vez**.

* **El Problema:** Si tienes un Jupyter Notebook abierto en la carpeta `99-notebooks/` que está usando la base de datos, e intentas correr un script de la carpeta `01-scripts/`, te arrojará un error de tipo `IOException: Could not set lock on file`.
* **La Solución:** Cierra la pestaña del notebook o dale a **"Restart Kernel"** en Jupyter para liberar la base de datos antes de ejecutar otro script en la terminal.