# CHANGELOG

Todos los cambios notables a este proyecto serán documentados en este archivo.

El formato es basado en: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Por favor, mantener los últimos cambios de primero (ejemplo: de lo más nuevo a lo más viejo).

### Fixed
### Added
### Changed
### Removed

---
## To do

- Completar cada uno de los scripts de Python para darle solución a los requerimientos.

---


# 2026-01-16

### Description:
Se hace el commit inicial después de crear el repositorio en GitHub. Se crea la estructura de directorios y archivos base.

### Added
- ```challenge.ipynb```: En la raíz del proyecto. Cuaderno de Jupyter para explicar a detalle la solución del reto, correr los scripts y expresar cualquier suposición y decisión tomada.

- ```src/```: Directorio principal del proyecto.

- ```documentation/```: En la raíz del proyecto. Tiene los archivos de documentación del proyecto.

- ```data/```: En la raíz del proyecto. Directorio de datos en donde serán ingestados los datos crudos de los tweets a procesar.

- ```q1_time.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 1:``` Enlistar las top 10 fechas donde hay más tweets, **optimizando el tiempo de ejecucción.**

- ```q1_memory.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 1:``` Enlistar las top 10 fechas donde hay más tweets, **optimizando el uso de memoria.**

- ```q2_time.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 2:``` Enlistar los top 10 emojis más usados con su respectivo conteo, **optimizando el tiempo de ejecucción.**

- ```q2_memory.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 2:``` Enlistar los top 10 emojis más usados con su respectivo conteo, **optimizando el uso de memoria.**

- ```q3_time.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 3:``` Enlistar el top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos, **optimizando el tiempo de ejecucción.**

- ```q3_memory.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 3:``` Enlistar el top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos, **optimizando el uso de memoria.**

- ```requirements.txt```: En la raíz del proyecto. Archivo de dependencias.

- ```.gitignore```: Archivo que le dice a git a lo que no debe hacerle seguimiento.

- ```.gitkeep```: Archivo dentro de la carpeta **data/** para que git haga el seguimiento de la carpeta así esté vacía.

- ```README.md```: Dentro del directorio documentation/. README del proyecto. Documento que explica a fondo el reto, los requerimientos y la forma para enviar la solución.

- ```CHANGELOG.md```: Dentro del directorio documentation/. CHANGELOG del proyecto. Documento que explica a detalle los cambios que se van realizando al proyecto.