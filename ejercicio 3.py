import tkinter as tk

def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def calcular_promedio(arr):
    n = len(arr)
    if n == 0:
        return 0
    suma = sum(arr)
    return suma / n

def calcular_suma(arr):
    return sum(arr)

def ingresar_elemento():
    elemento = int(entry.get())
    if elemento == 0:
        arr.sort(reverse=True)
        tamano = len(arr)
        promedio = calcular_promedio(arr)
        suma = calcular_suma(arr)
        resultado.config(text="Tamaño del arreglo: {}\nPromedio: {}\nSuma: {}".format(tamano, promedio, suma))
    else:
        arr.append(elemento)
        entry.delete(0, tk.END)

arr = []

window = tk.Tk()
window.title("Ordenamiento por Selección")
window.geometry("300x200")

label = tk.Label(window, text="Ingrese un elemento (0 para terminar):")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Ingresar", command=ingresar_elemento)
button.pack()

resultado = tk.Label(window)
resultado.pack()

window.mainloop()