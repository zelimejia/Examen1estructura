import tkinter as tk
import Cola as que

q = que.Colas()

def agregar_elemento():
    elemento = int(entry.get())
    if elemento == 0:
        print(arreglo)
    else:
        arreglo.append(elemento)
        q.enqueue(elemento)
        entry.delete(0, tk.END)

        
def vercola():
    tamanocola=q.__len__()
    resultado_tamañocola.config(text="El tamano de la cola es:.{}".format(tamanocola))
    verdatoscola=q.__repr__()
    print(verdatoscola)

def encolar():
    varencolar = int(entry_encolar.get())
    q.enqueue(varencolar)
    entry_encolar.delete(0, tk.END)
    
    
def descolar():
    q.dequeue()
   
arreglo = []



ventana = tk.Tk()
ventana.title("Ingreso y búsqueda de elementos")
ventana.geometry("800x400")

# Ingreso de elementos
label = tk.Label(ventana, text="Ingresa un número entero (0 para terminar):")
label.pack()

entry = tk.Entry(ventana)
entry.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack()

label_paravertamañocola = tk.Label(ventana, text="Presiona para ver tamaño de la cola, adicionalmente puede observar los datos de la cola en la seccion de consola")
label_paravertamañocola.pack()

boton_paravertamañocola = tk.Button(ventana, text="Tamaño Cola", command=vercola)
boton_paravertamañocola.pack()


resultado_tamañocola = tk.Label(ventana, text="")
resultado_tamañocola.pack()


label_encolar = tk.Label(ventana, text="Ingresa un número entero para encolar:")
label_encolar.pack()

entry_encolar = tk.Entry(ventana)
entry_encolar.pack()

boton_encolar = tk.Button(ventana, text="Encolar", command=encolar)
boton_encolar.pack()

boton_descolar = tk.Button(ventana, text="Descolar", command=descolar)
boton_descolar.pack()



ventana.mainloop()