# INFO081-ProyectoTrenes
## Resumen del Proyecto

Este proyecto es un **Sistema de Simulación de Tráfico Ferroviario** desarrollado para la Empresa de Ferrocarriles del Estado (EFE). El objetivo principal es simular el flujo ferroviario para permitir a un "Operario" controlar y analizar el movimiento de trenes, la gestión de estaciones y la definición de rutas.

La solución propuesta permite al operario crear, modificar y eliminar los componentes clave de la simulación (trenes, estaciones y rutas), ejecutar la simulación (que opera por eventos) y guardar o cargar el estado del sistema.

## Integrantes

* Eduardo Pezo
* Martin Arratia
* Armando Carrasco
* Rafael Hoyl
* Agustin Montero

## Indicadores del Sistema [RF07]

De acuerdo con el requerimiento **RF07**, el sistema debe mostrar al menos dos indicadores para la toma de decisiones. Los indicadores seleccionados se visualizan en la interfaz de "Indicadores del Sistema" y son:

1.  **Distancia al tren más cercano:** Muestra la proximidad de otros trenes en la vía.
2.  **Tiempo aproximado en llegar:** Estima el tiempo restante para que el tren alcance su próximo destino (ej. una estación).

## Persistencia de Datos

La persistencia de datos se gestionará utilizando tres formatos de archivos de texto plano, guardados en disco:

* **Formato txt:** Se usará para almacenar información simple, como reportes de errores o un registro de eventos relevantes ocurridos durante la simulación.
* **Formato csv:** Se empleará para guardar datos en formato de tabla estructurada, permitiendo comparar tiempos de viaje entre estaciones o el tiempo total para completar una ruta.
* **Formato json:** Será el formato principal para guardar la configuración del sistema (estaciones, rutas, horarios de trenes) y el estado completo de las simulaciones.

### Pasos para Ejecutar

1.  Asegúrese de tener **Python 3** y **Tkinter** instalados.
2.  Abra una terminal en la carpeta raíz del proyecto (la que contiene `main.py` y las carpetas `ui/`, `logic/`).
3.  Ejecute el archivo `main.py`:

```bash
# Ejemplo: Posicionarse en la carpeta raíz del proyecto
cd "C:\Usuario\ProyectoTrenes\INFO081-ProyectoTrenes\"

# Ejecutar el archivo principal
python main.py