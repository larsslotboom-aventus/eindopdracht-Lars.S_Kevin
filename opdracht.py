import tkinter as tk
from tkinter.ttk import *
from math import pi
import os

newdir = __file__.replace('\\' + os.path.basename(__file__), '')
os.chdir(newdir)


root = tk.Tk()
root.title("main menu")

def open_window_btw():
    def calculate():
        tarief = int(tarief_entry.get()) / 100
        prijs = float(prijs_entry.get())
        btwbedrag = tarief * prijs
        eindprijs = prijs + btwbedrag
        btwbedrag_label.config(text="btw bedrag: {:.2f}".format(btwbedrag))
        eindprijs_label.config(text="eind prijs: {:.2f}".format(eindprijs))

    btw = tk.Toplevel(root)
    btw.title("BTW berekenen")

    tarief_label = tk.Label(btw, text="tarief in percentage:")
    tarief_label.grid(row=0, column=0, padx=5, pady=5)

    tarief_entry = tk.Entry(btw)
    tarief_entry.grid(row=0, column=1, padx=5, pady=5)

    prijs_label = tk.Label(btw, text="prijs:")
    prijs_label.grid(row=1, column=0, padx=5, pady=5)

    prijs_entry = tk.Entry(btw)
    prijs_entry.grid(row=1, column=1, padx=5, pady=5)

    calculate_button = tk.Button(btw, text="Bereken", command=calculate)
    calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    btwbedrag_label = tk.Label(btw, text="btw bedrag: ")
    btwbedrag_label.grid(row=3, column=0, padx=5, pady=5)

    eindprijs_label = tk.Label(btw, text="eind prijs: ")
    eindprijs_label.grid(row=4, column=0, padx=5, pady=5)


def open_window_vierkant():
    def calculate():
        length = float(length_entry.get())
        width = float(width_entry.get())
        perimeter = 2 * (length + width)
        area = length * width
        perimeter_label.config(text="Omtrek: {:.2f}".format(perimeter))
        area_label.config(text="Oppervlakte: {:.2f}".format(area))
    
    vierkant = tk.Toplevel(root)
    vierkant.title("Vierkant berekeningen")
    
    length_label = tk.Label(vierkant, text="Lengte:")
    length_label.grid(row=0, column=0, padx=5, pady=5)
    
    length_entry = tk.Entry(vierkant)
    length_entry.grid(row=0, column=1, padx=5, pady=5)
    
    width_label = tk.Label(vierkant, text="Breedte:")
    width_label.grid(row=1, column=0, padx=5, pady=5)
    
    width_entry = tk.Entry(vierkant)
    width_entry.grid(row=1, column=1, padx=5, pady=5)
    
    calculate_button = tk.Button(vierkant, text="Bereken", command=calculate)
    calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    perimeter_label = tk.Label(vierkant, text="Omtrek: ")
    perimeter_label.grid(row=3, column=0, padx=5, pady=5)
    
    area_label = tk.Label(vierkant, text="Oppervlakte: ")
    area_label.grid(row=4, column=0, padx=5, pady=5)
    

def open_window_cirkel():
    def calculate():
        diameter = float(entry.get())
        circumference = pi * diameter
        area = pi * (diameter/2)**2
        result_label.config(text=f"Omtrek: {circumference:.2f}\nOppervlakte: {area:.2f}")

    cirkel = tk.Toplevel(root)
    cirkel.title("Bereken omtrek en oppervlakte van een cirkel")

    label = tk.Label(cirkel, text="Voer de diameter in:")
    label.grid(row=0, column=0, padx=5, pady=5)

    entry = tk.Entry(cirkel)
    entry.grid(row=0, column=1, padx=5, pady=5)

    button = tk.Button(cirkel, text="Bereken", command=calculate)
    button.grid(columnspan=2, padx=5, pady=5)

    result_label = tk.Label(cirkel, text="Omtrek:\nOppervlakte:")
    result_label.grid(columnspan=2, padx=5, pady=5)

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
button1 = tk.Button(root, text="BTW Berekening", width=18, command=open_window_btw)
button2 = tk.Button(root, text="Tijdberekening", width=18, command=open_window_tijdberekening)
button3 = tk.Button(root, text="Vierkant Berekeningen", width=18, command=open_window_vierkant)
button4 = tk.Button(root, text="circel Berekeningen", width=18, command=open_window_cirkel)

label.grid(row=0, column=0, columnspan=4)
button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=1, column=2, padx=5, pady=5)
button4.grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
