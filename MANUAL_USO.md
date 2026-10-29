# MANUAL DE USO
## Práctica N.º 4 – Seguridad Informática

### 1. Requisitos

- Python 3
- Visual Studio Code
- Flask
- Requests
- SQLite (incluido en Python)

### 2. Preparar el entorno

Abrir la carpeta del proyecto en Visual Studio Code.

Crear el entorno virtual:

```powershell
python -m venv venv
```

Activarlo en Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

### 3. Crear la base de datos

Ejecutar:

```powershell
python crear_bd.py
```

Se generará el archivo usuarios.db con los usuarios
de prueba y la tabla de auditoría.

Credenciales de laboratorio:

Usuario: admin
Contraseña: admin123

### 4. Ejecutar la aplicación vulnerable

En una terminal:

```powershell
python app_vulnerable.py
```

Abrir en el navegador:

http://127.0.0.1:5000

### 5. Ejecutar la aplicación segura

En otra terminal:

```powershell
python app_segura.py
```

Abrir en el navegador:

http://127.0.0.1:5001

### 6. Ejecutar las pruebas de SQL Injection

Con ambas aplicaciones funcionando, abrir
una tercera terminal y ejecutar:

```powershell
python ataque_sql_i.py
```

El script realiza tres pruebas en cada aplicación:

1. Credenciales correctas.
2. Contraseña incorrecta.
3. Intento controlado de SQL Injection.

Resultado esperado:

- Aplicación vulnerable: permite el acceso mediante SQL Injection.
- Aplicación segura: rechaza el mismo intento.

### 7. Ejecutar el escáner de red

```powershell
python escaneo_red.py
```

El escáner comprueba determinados puertos
de la computadora local (127.0.0.1).

Si la aplicación segura está funcionando,
el puerto 5001 debería aparecer abierto.

### 8. Consultar los registros de auditoría

Primero, realizar intentos de inicio de sesión
en la aplicación segura.

Después ejecutar:

```powershell
python ver_auditoria.py
```

El programa mostrará los registros almacenados,
incluyendo usuario, resultado, fecha y hora.

### 9. Medidas de seguridad implementadas

- Consultas SQL parametrizadas.
- Prevención de la inyección SQL demostrada.
- Registro de accesos permitidos y denegados.
- Escaneo de puertos limitado al entorno local.
- Separación entre aplicación vulnerable y segura.

### 10. Consideraciones éticas

Este proyecto es un laboratorio académico.

La aplicación vulnerable no debe publicarse
como un servicio accesible desde Internet.

Las pruebas deben realizarse únicamente
en sistemas propios o autorizados.