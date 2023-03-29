import tkinter as tk

def calculate():
    distance = float(distance_entry.get())
    speed = float(speed_entry.get())
    time = distance / speed
    time_label.config(text="Reistijd: {:.2f} uur".format(time))

root = tk.Tk()
root.title("Reistijd berekenen")

distance_label = tk.Label(root, text="Afstand (km):")
distance_label.grid(row=0, column=0, padx=5, pady=5)

distance_entry = tk.Entry(root)
distance_entry.grid(row=0, column=1, padx=5, pady=5)

speed_label = tk.Label(root, text="Snelheid (km/uur):")
speed_label.grid(row=1, column=0, padx=5, pady=5)

speed_entry = tk.Entry(root)
speed_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Bereken", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

time_label = tk.Label(root, text="Reistijd: ")
time_label.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()
