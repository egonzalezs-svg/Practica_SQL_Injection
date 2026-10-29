import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL
)
""")

cursor.execute(
    "INSERT OR IGNORE INTO usuarios (usuario, contrasena) VALUES (?, ?)",
    ("admin", "admin123")
)

cursor.execute(
    "INSERT OR IGNORE INTO usuarios (usuario, contrasena) VALUES (?, ?)",
    ("estudiante", "clave123")
)
# Tabla para registrar los intentos de acceso
cursor.execute("""
CREATE TABLE IF NOT EXISTS auditoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    resultado TEXT NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conexion.commit()
conexion.close()

print("Base de datos creada correctamente.")