import tkinter as tk
from math import pi

def calculate():
    diameter = float(entry.get())
    circumference = pi * diameter
    area = pi * (diameter/2)**2
    result_label.config(text=f"Omtrek: {circumference:.2f}\nOppervlakte: {area:.2f}")

root = tk.Tk()
root.title("Bereken omtrek en oppervlakte van een cirkel")

label = tk.Label(root, text="Voer de diameter in:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)

button = tk.Button(root, text="Bereken", command=calculate)
button.grid(columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="Omtrek:\nOppervlakte:")
result_label.grid(columnspan=2, padx=5, pady=5)

root.mainloop()
