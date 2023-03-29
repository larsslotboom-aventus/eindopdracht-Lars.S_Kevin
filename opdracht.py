import tkinter as tk
import os

newdir = __file__.replace('\\' + os.path.basename(__file__), '')
os.chdir(newdir)


root = tk.Tk()
root.title("main menu")

def open_window(winID):
    open("logica\btw.py").read()

label = tk.Label(root, text="main menu", font=('arial',20))
button1 = tk.Button(root, text="BTW Berekening", width=18, command=open_window(0))
button2 = tk.Button(root, text="Tijdberekening", width=18)
button3 = tk.Button(root, text="Vierkant Berekeningen", width=18)
button4 = tk.Button(root, text="circel Berekeningen", width=18)

label.grid(row=0, column=0, columnspan=4)
button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=1, column=2, padx=5, pady=5)
button4.grid(row=1, column=3, padx=5, pady=5)
root.mainloop()
