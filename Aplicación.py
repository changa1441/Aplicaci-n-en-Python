import tkinter as tk

def calcular_promedio():
    nota1 = float(entry_nota1.get())
    nota2 = float(entry_nota2.get())
    nota3 = float(entry_nota3.get())
    promedio = (nota1 + nota2 + nota3) / 3
    label_promedio.config(text=f"Promedio: {promedio:.2f}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Notas")

# Crear etiquetas y campos de entrada
label_nota1 = tk.Label(ventana, text="Nota Parcial 1:")
entry_nota1 = tk.Entry(ventana)
label_nota2 = tk.Label(ventana, text="Nota Parcial 2:")
entry_nota2 = tk.Entry(ventana)
label_nota3 = tk.Label(ventana, text="Nota Parcial 3:")
entry_nota3 = tk.Entry(ventana)
label_promedio = tk.Label(ventana, text="Promedio: ")

# Botón de cálculo
boton_calcular = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)

# Colocar elementos en la ventana
label_nota1.grid(row=0, column=0)
entry_nota1.grid(row=0, column=1)
label_nota2.grid(row=1, column=0)
entry_nota2.grid(row=1, column=1)
label_nota3.grid(row=2, column=0)
entry_nota3.grid(row=2, column=1)
boton_calcular.grid(row=3, column=0, columnspan=2)
label_promedio.grid(row=4, column=0, columnspan=2)

# Iniciar la aplicación
ventana.mainloop()
