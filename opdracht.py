import tkinter as tk

root = tk.Tk()

button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")
button4 = tk.Button(root, text="Button 4", height=6)

button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=1, column=0, padx=5, pady=5)
button3.grid(row=2, column=0, padx=5, pady=5)
button4.grid(row=0, column=1, rowspan=3, padx=5, pady=5)
root.mainloop()