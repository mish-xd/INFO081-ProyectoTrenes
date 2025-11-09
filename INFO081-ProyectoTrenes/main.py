#Este va a ser el archivo de donde vamos a llamar a todas las funciones de las otras carpetas
##probando ventana y paleta de colores

from tkinter import Tk,Label,Button
from config.colores import COLOR_FONDO,COLOR_TEXTO,COLOR_BOTON, COLOR_TEXTO_BOTON
from config.tamaño_ventana import ANCHO_VENTANA,ALTO_VENTANA

def iniciar_interfaz():
 #ventana principal
 ventana=Tk()
 ventana.title("Simulador")
 ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
 ventana.config(bg=COLOR_FONDO)

 #Etiqueta
 Label(ventana,text="Bienvenido",bg=COLOR_BOTON,fg=COLOR_TEXTO,font=("Segoe UI",16,"bold")).pack()
 Button(ventana,text="iniciar simulacion",bg=COLOR_BOTON,fg=COLOR_TEXTO_BOTON,font=("Segoe UI",12),width=20,height=2).pack()

 ventana.mainloop()

if __name__=="__main__":
 iniciar_interfaz()
