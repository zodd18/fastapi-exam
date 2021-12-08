# Tecnologías usadas

## Backend

(Directorio `backend`)

#### Framework
Se ha utilizado el framework FastAPI (Python 3) para la API REST.

#### Base de datos
En cuanto a la base de datos, se ha utilizado MongoDB (credenciales disponibles en `./backend/config/db.py`)

## Frontend

(Directorio `frontend`)

#### Cliente REST
Se han utilizado HTML5 y el framework Vue.js (JavaScript) para el cliente REST (directorio `rest_client`).

#### Cliente AJAX
Se han utilizado HTML5 y AJAX para el cliente AJAX (directorio `ajax_client`).

# Manual de usuario

## Instalación del backend

* Descargar e instalar [python3](https://www.python.org/downloads/) .

* Ejecutar el fichero `./backend/install.bat`
    - Alternativamente ejecutar:
        ```
        pip3 install -r ./backend/requirements.txt
        ```
        
## Ejecución

#### API REST
* Ejecutar el fichero `./backend/run.bat`
    - Alternativamente y estando dentro del directorio `./backend` ejecutar:
        ```
        uvicorn run:app --reload
        ```
    - El servidor se abrirá en `http://localhost:8000`
#### Cliente REST
* Abrir el fichero `./frontend/rest_client/index.html` en un navegador de preferencia (p. ej. [Firefox](https://www.mozilla.org/es-ES/firefox/new/)).

#### Cliente AJAX
* Abrir el fichero `./frontend/ajax_client/index.html` en un navegador de preferencia (p. ej. [Firefox](https://www.mozilla.org/es-ES/firefox/new/)).

## Documentación

La documentación de la API REST viene definida en la misma API, concretamente en `http://localhost:8000/docs` .
