# NOMBRE DEL PROYECTO
**Clasificacion de ataques cardiacos empleando el uso de Machine Learning**


## DESCRIPCIÓN DEL PROYECTO
Este proyecto consiste en el desarrollo de modelos empleando el uso de **Machine Learning** y el uso de la Feature Engineering, a traves de la creacion de diferentes Pipelines y Transformers, que permiten determinar la calidad de los modelos elaborados

## ESTRUCTURA DEL PROYECTO
```
heart-attack-clasificacion/
├── app/                    # Aplicacion creada con streamlit
├── data/                   # Datos limpios y transformados
├── models/                 # Archivos con los modelos creados
├── Notebooks/              # Jupyter Notebooks creados
├── python-version          # Version de python utilizada
├── Diccionario_Datos.md    # Informacion detallada del conjunto de datos
├── pyproject.toml          # Librerias utilizadas en el proyecto
├── requerements.text       # Librerias, dependencias empleadas
└── .venv/ (no incluido en la entrega)
```

## REQUISITOS
Para la correcta ejecución de este proyecto, es necesario contar con:
*   **Python**: Versión 3.11.
*   **Sistema Operativo**: Compatible con Windows, macOS o distribuciones de Linux.
*   **Gestor de paquetes**: Se puede utilizar `pip` o el gestor  `uv`.


## INSTALACION

Siga estos pasos de forma secuencial para preparar su entorno local y asegurar que el modelo funcione correctamente:

### 1. Clonar el repositorio
Primero, obtenga una copia local del proyecto ejecutando el siguiente comando en su terminal:

```bash
git clone (https://github.com/zaflocoX/heart-attack-clasificacion.git)
cd heart-attack-clasificacion
```
### 2. Crear el entorno virtual
Es fundamental aislar las librerías del proyecto para evitar conflictos de versiones. Puede realizarlo de dos formas:
*   **Con Python estándar:** `python -m venv .venv`
*   **Con uv (Recomendado):** `uv venv`

### 3. Sincronización de librerías y selección de Kernel
Una vez creado el entorno, debe instalar las dependencias y vincular el editor:

**Sincronizar librerías:**
*   Si utiliza **uv**, ejecute el siguiente comando para instalar automáticamente lo definido en el `pyproject.toml`:
        ```bash
        uv sync
        ```
*   Si utiliza **pip**, instale las librerías desde el archivo de requerimientos:
    ```bash
    pip install -r requirements.txt
    ```

### 5. Ejecutar los Notebooks en orden
Los cuadernos de notas están numerados para mantener la coherencia del flujo de datos. Debe ejecutarlos de forma secuencial:
1.  `01-carga_datos.ipynb`
2.  `02-analisis_exploratorio.ipynb`
3.  `03-AutoML_Pycaret.ipynb`
4.  `04-entrenamiento_modelos.ipynb`
5.  `05-lectura_modelo.ipynb`

# AUTOR(ES) 
*   **Autor:** Zamir Flores Cordoba
