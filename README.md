
-- INSTALAR PYTHON, AÑADIENDOLO A PATHS
    https://www.python.org/downloads/


-- INSTALAR WSL EN UNA POWER SHELL COMO ADMIN (vídeo ayuda: https://www.youtube.com/watch?v=ZO4KWQfUBBc)
    Tenemos que tener la virtualización activada: https://docs.docker.com/desktop/troubleshoot/topics/#virtualization

    $ wsl --install         *Aunque no hace falta, nos va a instalar Ubuntu automáticamente


-- INSTALAR DOCKER
    https://docs.docker.com/desktop/install/windows-install/


-- PARA NO TENER PROBLEMAS CON LAS VERSIONES VAMOS A USAR UN ENTORNO VIRTUAL

    $ pip install virtualenv

   Cambiamos el intérprete al entorno virtual: File-> Settings -> Project:FastAPI -> Python Interpreter -> Usamos el de la carpeta FastAPI\venv\Scripts\python.exe
    
   Para activarlo desde la terminal del proyecto: $ .\venv\Scripts\activate
   ¡SIEMPRE USAR LA CONSOLA CON EL ENTORNO VIRTUAL ACTIVADO! (sale (venv) al principio de cada línea)


-- INSTALAR FastAPI

    $pip install fastapi


-- INSTALAR UNICORN (va a lanzar la api)

    $ pip install uvicorn

--INSTALAR PYBSON

    $ pip install pybson

-- INSTALAR PYMONGO

    $ pip install pymongo    



LEVANTAR LA API:
   Ejecutar app.py o hacerlo por terminal:

    uvicorn app:app --host localhost --port 8000 --reload

Para acceder a la documentación de los servicios:
http://localhost:8000/docs
