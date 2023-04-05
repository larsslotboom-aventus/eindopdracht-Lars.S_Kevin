import tkinter as tk

def calculate():
    tarief = int(tarief_entry.get()) / 100
    prijs = float(prijs_entry.get())
    btwbedrag = tarief * prijs
    eindprijs = prijs + btwbedrag
    btwbedrag_label.config(text="btw bedrag: {:.2f}".format(btwbedrag))
    eindprijs_label.config(text="eind prijs: {:.2f}".format(eindprijs))

root = tk.Tk()
root.title("BTW berekenen")

tarief_label = tk.Label(root, text="tarief in percentage:")
tarief_label.grid(row=0, column=0, padx=5, pady=5)

tarief_entry = tk.Entry(root)
tarief_entry.grid(row=0, column=1, padx=5, pady=5)

prijs_label = tk.Label(root, text="prijs:")
prijs_label.grid(row=1, column=0, padx=5, pady=5)

prijs_entry = tk.Entry(root)
prijs_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Bereken", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

btwbedrag_label = tk.Label(root, text="btw bedrag: ")
btwbedrag_label.grid(row=3, column=0, padx=5, pady=5)

eindprijs_label = tk.Label(root, text="eind prijs: ")
eindprijs_label.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()
