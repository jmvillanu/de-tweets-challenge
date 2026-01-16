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

- Crear la función q2, q2_time y q2_memory

---

# 2026-01-16

### Description:
Se creó las funciones q2, q2_time y q2_memory. Normal, optimizando tiempo de ejecucion y optimizando uso de memoria, respectivamente.

### Added

- ```q2.py```: Se creó la función q2, obtiene los 10 emojis más populares.

- ```q2_time.py```: Se creó la función q2_time, paralelizando el proceso. Mejora tiempo de ejecucion y empeora uso de memoria.

- ```q2_memory.py```: Se creó la función q2_memory, mejora levemente el uso de memoria. No hay mucha diferencia con q2.

### Changed

1. ```challenge.ipynb```: Se probó la ejecución de la función q2, q2_time, q2_memory.

---
# 2026-01-16

### Description:
Se creó la función q1_memory en el archivo q1_memory.py, optimizando el uso de memoria.
### Added

- ```q1_memory.py```: Se creó la función q1_memory, buscando **optimizar el uso de memoria.** con respecto a la función inicial q1.

### Changed

1. ```challenge.ipynb```: Se probó la ejecución de la función q1_memory en cuanto a uso de memoria y también se obtuvo el valor en cuanto al tiempo de ejecución.

---

# 2026-01-16

### Description:
Se creó la función q1_time en el archivo q1_time.py, optimizando tiempo de ejecución.

### Added

- ```q1_time.py```: Se creó la función q1_time, buscando **optimizar el tiempo de ejecución.** con respecto a la función inicial q1.

### Changed

1. ```challenge.ipynb```: Se probó la ejecución de la función q1_time en cuanto a tiempo de ejecucion y también se obtuvo el valor en cuanto al uso de memoria. También se mejoró la documentación.

2. ```CHANGELOG.md```: Se corrigieron errores de escritura en el documento.

---

# 2026-01-16

### Description:
Se solucionó el requerimiento 1 en cuanto a obtener el top 10 de fechas con más tweets y sus username respectivos. No se ha realizado ninguna optimización, que también es parte del requerimiento.

### Added

- ```q1.py```: Archivo con la función q1 para solucionar el ```Requerimiento 1:``` Enlistar las top 10 fechas donde hay más tweets, mencionando el username que más tweet posteó para dicha fecha.

### Changed

1. ```challenge.ipynb```: Se probó la ejecución de la función q1 y se obtuvo el tiempo de ejecución y el uso de memoria.

2. ```requirements.txt```: Se ejecutó ```pip freeze > requirements.txt``` desde la terminal para actualizar las versiones de las dependencias en el archivo.

3. ```.gitignore```: Se agrega la carpeta data/ para que no se suban los datos al repositorio y __pycache__ para que el caché tampoco lo suba la repositorio.

---

# 2026-01-16

### Description:
Se hace el commit inicial después de crear el repositorio en GitHub. Se crea la estructura de directorios y archivos base.

### Added
- ```challenge.ipynb```: En la raíz del proyecto. Cuaderno de Jupyter para explicar a detalle la solución del reto, correr los scripts y expresar cualquier suposición y decisión tomada.

- ```src/```: Directorio principal del proyecto.

- ```documentation/```: En la raíz del proyecto. Tiene los archivos de documentación del proyecto.

- ```data/```: En la raíz del proyecto. Directorio de datos en donde serán ingestados los datos crudos de los tweets a procesar.

- ```q1_time.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 1:``` Enlistar las top 10 fechas donde hay más tweets, **optimizando el tiempo de ejecución.**

- ```q1_memory.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 1:``` Enlistar las top 10 fechas donde hay más tweets, **optimizando el uso de memoria.**

- ```q2_time.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 2:``` Enlistar los top 10 emojis más usados con su respectivo conteo, **optimizando el tiempo de ejecución.**

- ```q2_memory.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 2:``` Enlistar los top 10 emojis más usados con su respectivo conteo, **optimizando el uso de memoria.**

- ```q3_time.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 3:``` Enlistar el top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos, **optimizando el tiempo de ejecución.**

- ```q3_memory.py```: Dentro del directorio *src/*. Plantilla para solucionar el ```Requerimiento 3:``` Enlistar el top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos, **optimizando el uso de memoria.**

- ```requirements.txt```: En la raíz del proyecto. Archivo de dependencias.

- ```.gitignore```: Archivo que le dice a git a lo que no debe hacerle seguimiento.

- ```.gitkeep```: Archivo dentro de la carpeta **data/** para que git haga el seguimiento de la carpeta así esté vacía.

- ```README.md```: Dentro del directorio documentation/. README del proyecto. Documento que explica a fondo el reto, los requerimientos y la forma para enviar la solución.

- ```CHANGELOG.md```: Dentro del directorio documentation/. CHANGELOG del proyecto. Documento que explica a detalle los cambios que se van realizando al proyecto.