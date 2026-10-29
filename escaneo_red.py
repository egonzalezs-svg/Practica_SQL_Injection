import socket

# Escaneo autorizado de nuestra propia computadora
OBJETIVO = "127.0.0.1"

PUERTOS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    5000: "Flask vulnerable",
    5001: "Flask seguro",
    8080: "HTTP alternativo"
}

print("LABORATORIO DE SEGURIDAD INFORMÁTICA")
print("Escaneo básico de puertos")
print(f"Objetivo: {OBJETIVO}")
print("-" * 45)

for puerto, servicio in PUERTOS.items():
    conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexion.settimeout(1)

    resultado = conexion.connect_ex((OBJETIVO, puerto))

    if resultado == 0:
        print(f"Puerto {puerto}: ABIERTO - {servicio}")
    else:
        print(f"Puerto {puerto}: CERRADO O NO ACCESIBLE")

    conexion.close()

print("-" * 45)
print("Escaneo finalizado.")