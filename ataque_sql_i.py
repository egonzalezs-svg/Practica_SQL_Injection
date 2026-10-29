import requests

# Aplicaciones de nuestro laboratorio local
APLICACIONES = {
    "VULNERABLE": "http://127.0.0.1:5000/",
    "SEGURA": "http://127.0.0.1:5001/"
}

PRUEBAS = {
    "Credenciales correctas": {
        "usuario": "admin",
        "contrasena": "admin123"
    },
    "Contraseña incorrecta": {
        "usuario": "admin",
        "contrasena": "incorrecta123"
    },
    "SQL Injection": {
        "usuario": "admin' --",
        "contrasena": "incorrecta123"
    }
}

for nombre_app, url in APLICACIONES.items():
    print(f"\n===== APLICACIÓN {nombre_app} =====")

    for nombre_prueba, datos in PRUEBAS.items():
        try:
            respuesta = requests.post(
                url,
                data=datos,
                timeout=5
            )

            if "Acceso concedido" in respuesta.text:
                resultado = "ACCESO CONCEDIDO"
            elif "Usuario o contraseña incorrectos" in respuesta.text:
                resultado = "ACCESO DENEGADO"
            else:
                resultado = "RESPUESTA NO RECONOCIDA"

            print(
                f"{nombre_prueba}: {resultado} "
                f"(HTTP {respuesta.status_code})"
            )

        except requests.exceptions.RequestException as error:
            print(f"{nombre_prueba}: ERROR DE CONEXIÓN - {error}")

print("\nPruebas finalizadas.")