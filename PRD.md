## El Armario de Barbie
 # Descripción

El Armario de Barbie es una aplicación web creada para organizar y administrar prendas y accesorios de Barbie de una manera sencilla, visual y divertida.

La aplicación permite registrar, consultar, editar y eliminar prendas utilizando una base de datos SQLite.

El proyecto cuenta con una interfaz temática inspirada en Barbie, utilizando colores y elementos visuales relacionados con la marca.

 ## Objetivo

* Crear una aplicación web que permita administrar digitalmente un inventario de prendas y accesorios de Barbie mediante operaciones CRUD:

* Crear prendas.

* Consultar prendas.

* Editar prendas.

* Eliminar prendas.

 ## Funcionalidades

* Agregar nuevas prendas.
* Ver todas las prendas registradas.
* Editar la información de una prenda.
* Eliminar prendas.
* Agregar imágenes a las prendas.
* Registrar el precio de cada prenda.
* Registrar el color.
* Registrar el tipo de prenda.
* Registrar la temporada.
* Interfaz temática inspirada en Barbie.
* Almacenamiento de información mediante SQLite.

## Tecnologías utilizadas

* Python

* Flask

* SQLite

* HTML5

* CSS3

* JavaScript

* Visual Studio Code

* Git

## GitHub

 Estructura del proyecto
Armario-de-Barbie/
│
├── static/
│   ├── IMG/
│   │   └── imágenes de las prendas
│   │
│   └── style.css
│
├── templates/
│   ├── agregar.html
│   ├── editar.html
│   └── index.html
│
├── app.py
├── database.db
├── requirements.txt
└── README.md

## Instalación
1. Clonar el repositorio

Desde la terminal de Visual Studio Code:
git clone URL_DE_TU_REPOSITORIO
Después entra a la carpeta:

## cd Armario-de-Barbie

## 2. Crear un entorno virtual

En Windows:

python -m venv venv


Activar el entorno virtual:

venv\Scripts\activate


Si utilizas PowerShell:

.\venv\Scripts\Activate.ps1

## 3. Instalar las dependencias

Ejecuta:

pip install -r requirements.txt


Si todavía no existe el archivo requirements.txt, puedes instalar Flask directamente:

pip install flask


Y después crear el archivo con:

Flask

 Ejecutar la aplicación

Para iniciar la aplicación:

python app.py


Después abre en el navegador la dirección que indique Flask, normalmente:

http://127.0.0.1:5000

 Base de datos

El proyecto utiliza SQLite para almacenar la información de las prendas.

La base de datos se encuentra en:

database.db


## La tabla principal es:

* prendas

- Campos
- Campo	Descripción
- id	Identificador único
- Nombre de la prenda
- tipo	Tipo de prenda
- Color de la prenda
- Temporada
- Precio de la prenda
- Ruta de la imagen
 ## Funcionamiento
## El usuario puede realizar las siguientes operaciones:

        EL ARMARIO DE BARBIE
                  │
                  ▼
          ┌───────────────┐
          │ Ver prendas   │
          └───────┬───────┘
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
    Agregar     Editar    Eliminar
       │          │          │
       └──────────┼──────────┘
                  ▼
             SQLite

 ## Agregar una prenda

El usuario puede registrar:

- Nombre.

- Tipo.

- Color.

- Temporada.

- Precio.

- Imagen.

Los datos se almacenan en la base de datos.

 Editar una prenda

Cada prenda registrada tendrá una opción para editar su información.

El usuario podrá modificar los datos y guardar los cambios.

 Eliminar una prenda

El usuario podrá eliminar una prenda del inventario.

Se recomienda utilizar una confirmación antes de realizar la eliminación para evitar borrados accidentales.

 Imágenes

Las imágenes de las prendas se almacenan en:

static/IMG/


La base de datos guarda la ruta o nombre de la imagen correspondiente.

 Diseño

La aplicación utiliza una estética inspirada en Barbie.

Colores principales

Rosa.

Rosa claro.

Rosa oscuro.

Blanco.

Tonos pastel.

La interfaz utiliza tarjetas, botones y elementos visuales para presentar las prendas de forma clara y atractiva.

 Compatibilidad

La aplicación está diseñada para funcionar en navegadores modernos como:

Google Chrome.

Microsoft Edge.

Mozilla Firefox.

También se busca que la interfaz sea adaptable a diferentes tamaños de pantalla.

Requisitos del proyecto

Para ejecutar el proyecto es necesario tener instalado:

Python 3.

Visual Studio Code.

Git.

Un navegador web.

GitHub

Para subir el proyecto a GitHub:

git init


Agregar los archivos:

git add .


Crear el primer commit:

git commit -m "Primer commit - El Armario de Barbie"


Conectar el repositorio:

git remote add origin URL_DE_TU_REPOSITORIO


Subir el proyecto:

git branch -M main
git push -u origin main

 Proyecto académico

Proyecto: El Armario de Barbie
Tipo: Aplicación web CRUD
Backend: Flask
Base de datos: SQLite
Frontend: HTML, CSS y JavaScript
Control de versiones: Git y GitHub

 Estado del proyecto

En desarrollo

El proyecto puede ampliarse posteriormente con funcionalidades como:

 Búsqueda de prendas.

 Filtros por tipo, color o temporada.

 Estadísticas del armario.

 Sistema de usuarios.

 Prendas favoritas.

 Almacenamiento en la nube.

 Mejoras para dispositivos móviles.
