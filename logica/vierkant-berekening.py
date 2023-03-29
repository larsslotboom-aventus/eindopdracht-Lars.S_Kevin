import tkinter as tk
def open_window_vierkant():
    def calculate():
        length = float(length_entry.get())
        width = float(width_entry.get())
        perimeter = 2 * (length + width)
        area = length * width
        perimeter_label.config(text="Omtrek: {:.2f}".format(perimeter))
        area_label.config(text="Oppervlakte: {:.2f}".format(area))
    
    root = tk.Tk()
    root.title("Vierkant berekeningen")
    
    length_label = tk.Label(root, text="Lengte:")
    length_label.grid(row=0, column=0, padx=5, pady=5)
    
    length_entry = tk.Entry(root)
    length_entry.grid(row=0, column=1, padx=5, pady=5)
    
    width_label = tk.Label(root, text="Breedte:")
    width_label.grid(row=1, column=0, padx=5, pady=5)
    
    width_entry = tk.Entry(root)
    width_entry.grid(row=1, column=1, padx=5, pady=5)
    
    calculate_button = tk.Button(root, text="Bereken", command=calculate)
    calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    perimeter_label = tk.Label(root, text="Omtrek: ")
    perimeter_label.grid(row=3, column=0, padx=5, pady=5)
    
    area_label = tk.Label(root, text="Oppervlakte: ")
    area_label.grid(row=4, column=0, padx=5, pady=5)
    
    root.mainloop()
    