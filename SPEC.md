 SPEC — El Armario de Barbie

Technical Specification

Especificación técnica de la aplicación web El Armario de Barbie.

 1. Información técnica
Elemento	Tecnología
Lenguaje	Python
Framework	Flask
Base de datos	SQLite
Frontend	HTML5
Estilos	CSS3
Interactividad	JavaScript
Editor	Visual Studio Code
Control de versiones	Git
Repositorio	GitHub
 2. Arquitectura

La aplicación utilizará una arquitectura web basada en Flask.

                    USUARIO
                       │
                       ▼
                ┌─────────────┐
                │  Navegador  │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │    Flask    │
                │   app.py    │
                └──────┬──────┘
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
        ┌───────────┐     ┌───────────┐
        │ Templates │     │  SQLite   │
        │   HTML    │     │ database  │
        └───────────┘     └───────────┘

 3. Estructura del proyecto
Armario-de-Barbie/
│
├── docs/
│   ├── PRD.md
│   └── SPEC.md
│
├── static/
│   ├── IMG/
│   │   └── imágenes de prendas
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

 4. Base de datos

El sistema utilizará SQLite.

Archivo:

database.db


Tabla principal:

prendas

 5. Estructura de la tabla
Campo	Tipo	Restricciones	Descripción
id	INTEGER	PRIMARY KEY	Identificador
nombre	TEXT	NOT NULL	Nombre
tipo	TEXT	NOT NULL	Tipo
color	TEXT	NOT NULL	Color
temporada	TEXT	NOT NULL	Temporada
precio	REAL	NOT NULL	Precio
imagen	TEXT	NULL	Imagen
 6. SQL de creación
CREATE TABLE prendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    color TEXT NOT NULL,
    temporada TEXT NOT NULL,
    precio REAL NOT NULL,
    imagen TEXT
);

 7. Rutas Flask
Página principal
GET /

Función

Mostrar todas las prendas registradas.

Template
templates/index.html

Agregar prenda — formulario
GET /agregar

Función

Mostrar el formulario para registrar una nueva prenda.

Template
templates/agregar.html

Agregar prenda — guardar
POST /agregar

Función

Recibir los datos del formulario y almacenarlos en SQLite.

Datos
nombre
tipo
color
temporada
precio
imagen

Editar prenda
GET /editar/<id>

Función

Obtener los datos de una prenda y mostrarlos en el formulario de edición.

Template
templates/editar.html

Actualizar prenda
POST /editar/<id>

Función

Actualizar los datos de la prenda seleccionada.

Eliminar prenda
GET /eliminar/<id>

Función

Eliminar una prenda de la base de datos.

Para una implementación futura se recomienda utilizar POST para operaciones destructivas.

 8. Flujo de creación
Usuario
   │
   ▼
GET /agregar
   │
   ▼
Formulario
   │
   ▼
POST /agregar
   │
   ▼
Validación
   │
   ├───────────────┐
   │               │
 Inválido        Válido
   │               │
   ▼               ▼
 Error          INSERT
                   │
                   ▼
                SQLite
                   │
                   ▼
              Página inicio

 9. Flujo de edición
Usuario
   │
   ▼
Seleccionar "Editar"
   │
   ▼
GET /editar/<id>
   │
   ▼
Consultar SQLite
   │
   ▼
Mostrar formulario
   │
   ▼
POST /editar/<id>
   │
   ▼
UPDATE
   │
   ▼
SQLite
   │
   ▼
Página principal

🗑️ 10. Flujo de eliminación
Usuario
   │
   ▼
Seleccionar "Eliminar"
   │
   ▼
Confirmación
   │
   ├── Cancelar
   │      │
   │      ▼
   │    Finalizar
   │
   └── Confirmar
          │
          ▼
        DELETE
          │
          ▼
        SQLite
          │
          ▼
     Página principal

 11. Formulario de creación

El formulario de agregar.html deberá contener:

Nombre
[________________________]

Tipo
[________________________]

Color
[________________________]

Temporada
[________________________]

Precio
[________________________]

Imagen
[ Seleccionar archivo ]

[ GUARDAR PRENDA ]

 12. Formulario de edición

El formulario editar.html deberá cargar automáticamente los datos actuales de la prenda.

Nombre
[ Vestido rosa ]

Tipo
[ Vestido ]

Color
[ Rosa ]

Temporada
[ Primavera ]

Precio
[ 25.00 ]

Imagen
[ Imagen actual ]

[ GUARDAR CAMBIOS ]

 13. Vista principal

La página index.html mostrará las prendas utilizando tarjetas.

┌──────────────────────────┐
│                          │
│         IMAGEN           │
│                          │
├──────────────────────────┤
│ Vestido Rosa             │
│                          │
│ Tipo: Vestido            │
│ Color: Rosa              │
│ Temporada: Primavera     │
│ Precio: $25.00           │
│                          │
│ [ EDITAR ] [ ELIMINAR ]  │
└──────────────────────────┘


Las tarjetas deberán organizarse mediante CSS Grid o Flexbox.

 14. Diseño visual

La interfaz deberá tener una temática inspirada en Barbie.

Paleta de colores
:root {
    --rosa-principal: #ff69b4;
    --rosa-claro: #ffd6e7;
    --rosa-oscuro: #d63384;
    --blanco: #ffffff;
    --fondo: #fff5fa;
    --texto: #4a3040;
}

Componentes

La interfaz deberá incluir:

Encabezado.

Título.

Botón para agregar.

Tarjetas de prendas.

Formularios.

Botones de acción.

Mensajes de error.

Mensajes de confirmación.

Diseño responsive.

 15. Gestión de imágenes

Las imágenes estarán almacenadas en:

static/IMG/


La base de datos deberá guardar únicamente la ruta o nombre del archivo.

Ejemplo:

IMG/vestido_rosa.jpg


En Flask/Jinja:

<img
    src="{{ url_for('static', filename=prenda.imagen) }}"
    alt="{{ prenda.nombre }}"
>

 16. Validaciones

El backend deberá validar la información recibida.

Nombre

No puede estar vacío.

Tipo

No puede estar vacío.

Color

No puede estar vacío.

Temporada

No puede estar vacía.

Precio

Debe ser un número.

No debe aceptar valores negativos.

Ejemplo:

if precio < 0:
    # Mostrar mensaje de error

 17. Seguridad básica

Se deberán aplicar buenas prácticas básicas:

Validar los datos recibidos.

Utilizar consultas SQL parametrizadas.

Evitar concatenar directamente datos del usuario en consultas SQL.

Validar las imágenes subidas.

Limitar el tamaño de las imágenes.

Utilizar una SECRET_KEY segura.

No guardar contraseñas ni información sensible en el repositorio.

 18. Dependencias

El archivo requirements.txt deberá contener:

Flask


Instalación:

pip install -r requirements.txt

 19. Ejecución

Para ejecutar el proyecto:

python app.py


La aplicación estará disponible normalmente en:

http://127.0.0.1:5000

 20. Pruebas funcionales
Prueba	Resultado esperado
Agregar prenda	La prenda aparece en el inventario
Consultar prendas	Se muestran las prendas guardadas
Editar prenda	Los cambios se guardan
Eliminar prenda	La prenda desaparece
Agregar imagen	La imagen se muestra
Precio inválido	Se muestra un error
Campo vacío	Se solicita completar el campo
Reiniciar aplicación	Los datos permanecen
 21. Criterios técnicos de aceptación

 Flask inicia correctamente.

 SQLite funciona correctamente.

 Se pueden crear prendas.

 Se pueden consultar prendas.

 Se pueden editar prendas.

 Se pueden eliminar prendas.

 Las imágenes funcionan.

 Los precios se almacenan correctamente.

 Los campos obligatorios se validan.

 La interfaz tiene diseño temático.

 El diseño es responsive.

 El proyecto puede ejecutarse desde Visual Studio Code.

 El proyecto puede almacenarse en GitHub.

 22. Definición de terminado

El proyecto se considerará terminado cuando todas las operaciones CRUD funcionen correctamente y los datos se almacenen de forma persistente en SQLite.

Además, el código deberá estar organizado, documentado y disponible en el repositorio de GitHub.

 Proyecto

El Armario de Barbie

Backend:     Python + Flask
Frontend:    HTML + CSS + JavaScript
Database:    SQLite
Editor:      Visual Studio Code
Versionado:  Git + GitHub


 El Armario de Barbie — Organiza tu colección de una forma divertida y visual.