# Manual de usuario

## Instalación del backend

* Descargar e instalar [python3](https://www.python.org/downloads/)

* Ejecutar el fichero ```./backend/install.bat```
    - Alternativamente ejecutar:
        ```
        pip3 install -r ./backend/requirements.txt
        ```

## Ejecución


### Api REST
* Ejecutar el fichero ```./backend/run.bat```
    - Alternativamente y estando dentro del directorio ```./backend``` ejecutar:
        ```
        uvicorn run:app --reload
        ```

### Cliente REST
* Abrir el fichero ```./frontend/index.html``` en un navegador de preferencia (p. ej. [Firefox](https://www.mozilla.org/es-ES/firefox/new/))
