import tkinter as tk
from tkinter.ttk import *
import os

newdir = __file__.replace('\\' + os.path.basename(__file__), '')
os.chdir(newdir)


root = tk.Tk()
root.title("main menu")

def open_window_tijdberekening():
    def calculate():
        distance = float(distance_entry.get())
        speed = float(speed_entry.get())
        time = distance / speed
        time_label.config(text="Reistijd: {:.2f} uur".format(time))

    tijdberekening = tk.Toplevel(root)
    tijdberekening.title("Reistijd berekenen")

    distance_label = tk.Label(tijdberekening, text="Afstand (km):")
    distance_label.grid(row=0, column=0, padx=5, pady=5)

    distance_entry = tk.Entry(tijdberekening)
    distance_entry.grid(row=0, column=1, padx=5, pady=5)

    speed_label = tk.Label(tijdberekening, text="Snelheid (km/uur):")
    speed_label.grid(row=1, column=0, padx=5, pady=5)

    speed_entry = tk.Entry(tijdberekening)
    speed_entry.grid(row=1, column=1, padx=5, pady=5)

    calculate_button = tk.Button(tijdberekening, text="Bereken", command=calculate)
    calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    time_label = tk.Label(tijdberekening, text="Reistijd: ")
    time_label.grid(row=3, column=0, padx=5, pady=5)


label = tk.Label(root, text="main menu", font=('arial',20))
button1 = tk.Button(root, text="BTW Berekening", width=18)
button2 = tk.Button(root, text="Tijdberekening", width=18, command=open_window_tijdberekening)
button3 = tk.Button(root, text="Vierkant Berekeningen", width=18)
button4 = tk.Button(root, text="circel Berekeningen", width=18)

label.grid(row=0, column=0, columnspan=4)
button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=1, column=2, padx=5, pady=5)
button4.grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
