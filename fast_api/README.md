# FASTAPI
## Creacion del entorno virtual
1. instalar la libreria del entorno virtual: ````pip install virtualenv````
2. creacion de entorno virtual ````python -m virtualenv [NOMBRE ex:"venv"]````
3. verificamos el python general ````pip freeze```` tienen que salir varias librerias.
4. Entro a mi entorno virtual (EN WINDOWS desde GIT-BASH) ````source venv/Script/activate```` y sale el nombre del entorno virtual en mi linea de comandos.

## Instalar FastAPI
1. Instalacion de FastAPI ````pip install fastapi uvicorn````

## entrypoint.py
````py
from fastapi import FastAPI
app = FastAPI()
````
- Iniciar servidor uvicorn ````uvicorn entrypoint:app````