import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep", # esto es para CI/CD cuando se use github actions
    f"src/{project_name}/__init__.py", # crea scripts vacios
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", # rutas, parámetros globales
    "dvc.yaml", # pipeline de DVC
    "params.yaml", # hiperparametros del modelo
    "requirements.txt", # paquetes a instalar
    "setup.py", # construye paquete de python distribuible llamado "cnnClassifier"
                # y al correr el requirements.txt se instala dicho paquete (en modo editable)
    "research/trials.ipynb", #experimentos rápidos
    "templates/index.html" #serving/front end ...flask api/fastAPI

]


# Creación de carpetas y archivos
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
