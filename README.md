# Práctica N.º 4 – Seguridad Informática

## Laboratorio de SQL Injection con Python, Flask y SQLite

### Descripción

Este proyecto académico demuestra una vulnerabilidad de
inyección SQL (SQL Injection) en una aplicación web desarrollada
con Python, Flask y SQLite.

Incluye una aplicación vulnerable, una versión segura,
un script de pruebas de SQL Injection, un escáner básico
de puertos y un sistema de auditoría de accesos.

## Objetivo

Demostrar los riesgos de SQL Injection y comprobar cómo
las consultas SQL parametrizadas permiten prevenir
la manipulación de las consultas mediante entradas maliciosas.

## Tecnologías utilizadas

- Python
- Flask
- SQLite
- Requests
- Visual Studio Code

## Archivos del proyecto

- app_vulnerable.py: aplicación web vulnerable a SQL Injection.
- app_segura.py: aplicación protegida mediante consultas parametrizadas.
- crear_bd.py: creación de la base de datos SQLite.
- ataque_sql_i.py: pruebas automatizadas de SQL Injection.
- escaneo_red.py: escaneo básico de puertos locales.
- ver_auditoria.py: consulta de registros de auditoría.
- requirements.txt: dependencias del proyecto.
- MANUAL_USO.md: instrucciones de instalación y ejecución.

## Resultados obtenidos

La aplicación vulnerable permitió el acceso mediante una
inyección SQL sin utilizar la contraseña correcta.

La aplicación segura rechazó el mismo intento después de
implementar consultas parametrizadas.

También se comprobó el funcionamiento del escáner de
puertos y del registro de accesos permitidos y denegados.

## Consideraciones éticas

Este proyecto fue desarrollado exclusivamente con fines
académicos, en un entorno local y controlado.

Las pruebas de seguridad deben realizarse únicamente
sobre sistemas propios o con autorización expresa.