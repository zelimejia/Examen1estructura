import tkinter as tk

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def process_input():
    input_text = input_entry.get()
    try:
        num = int(input_text)
        if num == 0:
            bubble_sort(data)
            display_sorted_data()
        else:
            data.append(num)
            input_entry.delete(0, tk.END)
    except ValueError:
        input_entry.delete(0, tk.END)

def display_sorted_data():
    sorted_data_label['text'] = "Arreglo ordenado: " + ", ".join(map(str, data))
    max_value_label['text'] = "Elemento de mayor valor: " + str(max(data))
    min_value_label['text'] = "Elemento de menor valor: " + str(min(data))
    size_label['text'] = "Tamaño del arreglo: " + format(len(data))

data = []

window = tk.Tk()
window.title("Ordenamiento")
window.geometry("300x200")

input_label = tk.Label(window, text="Ingrese un número (0 para finalizar):")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

submit_button = tk.Button(window, text="Agregar", command=process_input)
submit_button.pack()

sorted_data_label = tk.Label(window, text="Arreglo ordenado:")
sorted_data_label.pack()

max_value_label = tk.Label(window, text="Elemento de mayor valor:")
max_value_label.pack()

min_value_label = tk.Label(window, text="Elemento de menor valor:")
min_value_label.pack()

size_label = tk.Label(window, text="Tamaño del arreglo: ")
size_label.pack()

window.mainloop()


