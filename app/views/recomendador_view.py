import tkinter as tk
from tkinter import ttk

# ==============
#      VIEW          
# ==============
class RecomendadorLivrosView(tk.Frame):
    def __init__(self, controller):
        # Inicializando o frame que englobará todos os outros widgets da janela do recomendador
        tk.Frame.__init__(self)
        self.controller = controller
        self.pack(padx=10, pady=10)
        
        # =====  Widgets  ======
        # Frames
        self.frame_livros = tk.Frame(self)
        self.frame_livros.grid(column=0, row=0)
        self.frame_recomendados = tk.Frame(self)
        self.frame_recomendados.grid(column=0, row=1)
        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.grid(column=0, row=2)
        
        # Labels
        self.label_livros = tk.Label(self.frame_livros, text="Selecione sua leitura atual: ")
        self.label_livros.pack()
        self.label_recomendados = tk.Label(self.frame_recomendados, text="Livros recomendados: ")
        self.label_recomendados.pack()
        
        # Buttons
        self.button_recomendar = tk.Button(self.frame_buttons, text="Recomendar", command=self.recomendar)
        self.button_recomendar.pack(side="left")
        self.button_limpar = tk.Button(self.frame_buttons, text="Limpar", command=self.limpar)
        self.button_limpar.pack(side="left")

        # Combobox
        self.combobox_livros_var = tk.StringVar()
        lista_livros = self.controller.listar_livros() # Obtém a lista a ser mostrada no combobox
        self.combobox_livros = ttk.Combobox(
            self.frame_livros,
            width=100,
            textvariable=self.combobox_livros_var,
            values=lista_livros,
            state="readonly")
        self.combobox_livros.pack()
        
        # Listbox
        self.listbox_recomendados = tk.Listbox(self.frame_recomendados, width=50)
        self.listbox_recomendados.pack()

    def atualizar_listbox(self, lista):
        self.listbox_recomendados.delete(0, tk.END)
        for item in lista:
            self.listbox_recomendados.insert(tk.END, item)
    
    def recomendar(self):
        titulo = self.combobox_livros_var.get()
        if titulo:
            self.controller.atualizar_recomendados(titulo)
    
    def limpar(self):
        self.controller.limpar_listbox()