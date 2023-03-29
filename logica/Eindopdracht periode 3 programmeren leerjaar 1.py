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
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Bereken", command=calculate)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()