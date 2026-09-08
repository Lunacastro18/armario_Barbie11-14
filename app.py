from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)



def conectar_db():
    conexion = sqlite3.connect("database.db")
    conexion.row_factory = sqlite3.Row
    return conexion



def crear_tabla():
    conexion = sqlite3.connect("database.db")

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS prendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tipo TEXT NOT NULL,
            color TEXT NOT NULL,
            temporada TEXT NOT NULL,
            precio REAL NOT NULL,
            imagen TEXT
        )
    """)

    conexion.commit()
    conexion.close()



@app.route("/")
def inicio():
    conexion = conectar_db()

    prendas = conexion.execute(
        "SELECT * FROM prendas"
    ).fetchall()

    conexion.close()

    return render_template("index.html", prendas=prendas)



@app.route("/agregar", methods=["GET", "POST"])
def agregar():

    if request.method == "POST":

        nombre = request.form["nombre"]
        tipo = request.form["tipo"]
        color = request.form["color"]
        temporada = request.form["temporada"]
        precio = request.form["precio"]
        imagen = request.form["imagen"]

        conexion = conectar_db()

        conexion.execute("""
            INSERT INTO prendas
            (nombre, tipo, color, temporada, precio, imagen)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            nombre,
            tipo,
            color,
            temporada,
            precio,
            imagen
        ))

        conexion.commit()
        conexion.close()

        return redirect("/")

    return render_template("agregar.html")



@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    conexion = conectar_db()

    if request.method == "POST":

        nombre = request.form["nombre"]
        tipo = request.form["tipo"]
        color = request.form["color"]
        temporada = request.form["temporada"]
        precio = request.form["precio"]
        imagen = request.form["imagen"]

        conexion.execute("""
            UPDATE prendas
            SET nombre = ?,
                tipo = ?,
                color = ?,
                temporada = ?,
                precio = ?,
                imagen = ?
            WHERE id = ?
        """, (
            nombre,
            tipo,
            color,
            temporada,
            precio,
            imagen,
            id
        ))

        conexion.commit()
        conexion.close()

        return redirect("/")

    prenda = conexion.execute(
        "SELECT * FROM prendas WHERE id = ?",
        (id,)
    ).fetchone()

    conexion.close()

    return render_template(
        "editar.html",
        prenda=prenda
    )



@app.route("/eliminar/<int:id>")
def eliminar(id):

    conexion = conectar_db()

    conexion.execute(
        "DELETE FROM prendas WHERE id = ?",
        (id,)
    )

    conexion.commit()
    conexion.close()

    return redirect("/")



crear_tabla()


if __name__ == "__main__":
    app.run(debug=True)