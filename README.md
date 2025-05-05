# Consumo de APIs

Este proyecto es una aplicación web desarrollada con Django que permite consultar información geográfica y climática en tiempo real utilizando APIs públicas.

## Funcionalidades

1. **Consulta de Provincias, Departamentos y Localidades**:
   - Utiliza la API de georreferenciación de datos.gob.ar para obtener información sobre provincias, departamentos y localidades de Argentina.
   - Los usuarios pueden seleccionar una provincia, luego un departamento y finalmente una localidad desde un formulario interactivo en la página principal.

2. **Consulta del Clima**:
   - Integra la API de OpenWeatherMap para obtener información climática en tiempo real.
   - A partir de la localidad seleccionada, se consulta su latitud y longitud para obtener datos como temperatura, sensación térmica, condiciones climáticas, entre otros.

3. **Interfaz de Usuario Interactiva**:
   - La página principal incluye un formulario dinámico que actualiza los departamentos y localidades en función de las selecciones previas.
   - Utiliza JavaScript para realizar solicitudes asíncronas (AJAX) y actualizar los datos sin recargar la página.

4. **Estructura del Proyecto**:
   - El proyecto está organizado en una aplicación llamada `clima`, que contiene las vistas, URLs, plantillas y lógica necesaria para las funcionalidades mencionadas.
   - La configuración del proyecto incluye la clave de API de OpenWeatherMap y está preparada para manejar plantillas y archivos estáticos.

5. **Endpoints**:
   - `/departamentos/`: Devuelve los departamentos de una provincia seleccionada.
   - `/localidades/`: Devuelve las localidades de un departamento seleccionado.
   - `/clima/`: Devuelve la información climática de una localidad seleccionada.

## Requisitos

- Python 3.10 o superior
- Django 5.2
- Dependencias adicionales listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio.
2. Crear un entorno virtual e instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configurar la clave de API de OpenWeatherMap en el archivo `settings.py`.
4. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso

Acceder a la aplicación en `http://127.0.0.1:8000/` y utilizar el formulario para consultar información geográfica y climática.