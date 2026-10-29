import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute("""
    SELECT id, usuario, resultado, fecha_hora
    FROM auditoria
    ORDER BY id DESC
""")

registros = cursor.fetchall()

print("\nREGISTRO DE AUDITORÍA")
print("-" * 65)

if registros:
    for registro in registros:
        print(
            f"ID: {registro[0]} | "
            f"Usuario: {registro[1]} | "
            f"Resultado: {registro[2]} | "
            f"Fecha: {registro[3]}"
        )
else:
    print("No existen registros de auditoría.")

conexion.close()