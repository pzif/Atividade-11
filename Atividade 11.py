import tkinter as tk

root = tk.Tk()

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Abrir")
file_menu.add_command(label="Salvar")
menubar.add_cascade(label="Arquivo", menu=file_menu)

text = tk.Text(root, wrap="word")
scrollbar = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

scrollbar.config(orient=tk.VERTICAL, command=text.yview)

root.mainloop()
