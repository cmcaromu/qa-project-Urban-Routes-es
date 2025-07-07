👤 Nombre: Carolina Muñoz Correa
🧾 Cohorte: Nº 29
🚕 PROYECTO URBAN ROUTES Sprint 8

Bienvenido a Urban Routes, un entorno de pruebas automatizadas diseñado para validar el correcto funcionamiento del proceso de solicitud de taxis dentro de la plataforma.
Desde la elección de la tarifa adecuada, el ingreso de datos del usuario, hasta la inclusión de servicios adicionales como mantas o helados, este proyecto reproduce el flujo completo tal como lo viviría un usuario real.

🧰 REQUISITOS

Para asegurar el funcionamiento adecuado del proyecto, necesitas contar con lo siguiente:

Python instalado en tu sistema,
Selenium para la automatización del navegador,
Pytest como framework de pruebas,
Acceso al entorno funcional de Urban Routes.

⚙️ INSTALACIÓN

Antes de comenzar, verifica que tengas configurado lo siguiente:

Python correctamente instalado,
Pytest integrado en tu entorno de desarrollo (como PyCharm),
Git para el manejo del repositorio,
Las dependencias necesarias (Selenium y Requests) instaladas,
El repositorio clonado en tu máquina local,
ChromeDriver disponible para controlar el navegador desde Selenium,

📂 Contenido del Proyecto

Este repositorio incluye los scripts principales de pruebas automatizadas que validan cada paso del flujo de la aplicación Urban Routes.
Se testean todos los puntos clave del proceso de solicitud de un taxi, desde el inicio hasta la confirmación final.

Funciones automatizadas incluidas:

Ingreso de dirección de origen y destino,
Selección de tarifa (como la opción Comfort),
Registro y verificación de número telefónico,
Asociación de una tarjeta de crédito como método de pago,
Envío de un mensaje personalizado al conductor,

Activación de servicios adicionales:

Mantas y pañuelos,
Helados,
Búsqueda activa de taxis y verificación visual del estado en pantalla,
Estas pruebas permiten garantizar que el recorrido del usuario se lleva a cabo sin errores, replicando una experiencia real en el navegador.

🗂️ Archivo data.py

El archivo data.py contiene todos los datos de entrada y configuraciones necesarias para ejecutar correctamente las pruebas.

Incluye:

Direcciones de prueba (origen y destino),
Número de teléfono simulado para validación,
Datos de tarjeta de crédito (número, CVV),
Mensajes predefinidos para el conductor,
URL del servidor de pruebas de Urban Routes,
Centralizar estos datos permite mantener limpio el código principal y simplifica futuras modificaciones.

▶️ Ejecución de las pruebas automatizadas

Cómo correr las pruebas:

Ejecutar todas las pruebas:
pytest

Ejecutar una prueba en específico:
pytest nombre_del_archivo.py

Para ver un informe detallado:
pytest -v

✅ Casos de prueba contemplados:

Ingreso de direcciones,
Selección de tarifa y modo personal,
Verificación del número telefónico,
Agregado de método de pago con tarjeta,
Activación de servicios (mantas, pañuelos, helados),
Envío de un comentario al conductor,
Validación del estado "Buscando taxi" tras la solicitud.

ℹ️ Notas adicionales:

Las pruebas requieren una conexión activa a internet,
Algunas validaciones, como el código de verificación telefónica, se simulan mediante funciones auxiliares
Se recomienda usar la versión más reciente de Google Chrome.
