from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Laboratorio SQL Injection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eaf0f6;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .contenedor {
            background: white;
            padding: 35px;
            border-radius: 12px;
            width: 350px;
            box-shadow: 0 4px 15px #0002;
            text-align: center;
        }
        input, button {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            box-sizing: border-box;
        }
        button {
            background: #1769aa;
            color: white;
            border: none;
            cursor: pointer;
        }
        .mensaje {
            margin-top: 15px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="contenedor">
        <h2>Seguridad Informática</h2>
        <h3>Laboratorio SQL Injection</h3>

        <form method="POST">
            <input type="text" name="usuario"
                   placeholder="Usuario" required>

            <input type="password" name="contrasena"
                   placeholder="Contraseña" required>

            <button type="submit">Iniciar sesión</button>
        </form>

        <p class="mensaje">{{ mensaje }}</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def inicio():
    mensaje = ""

    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        contrasena = request.form.get("contrasena", "")

        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        consulta = (
            "SELECT * FROM usuarios "
            "WHERE usuario = ? AND contrasena = ?"
        )

        try:
            cursor.execute(consulta, (usuario, contrasena))
            resultado = cursor.fetchone()

            if resultado:
                mensaje = "Acceso concedido"
                estado = "ACCESO PERMITIDO"
            else:
                mensaje = "Usuario o contraseña incorrectos"
                estado = "ACCESO DENEGADO"

            cursor.execute(
                """
                INSERT INTO auditoria (usuario, resultado)
                VALUES (?, ?)
                """,
                (usuario, estado)
            )

            conexion.commit()

        except sqlite3.Error as error:
            mensaje = "Error al procesar la consulta"
            print("Error de base de datos:", error)

        finally:
            conexion.close()

    return render_template_string(HTML, mensaje=mensaje)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False
    )