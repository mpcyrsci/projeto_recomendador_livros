import tkinter as tk
from app.views.recomendador_view import RecomendadorLivrosView

# ==============
#      VIEW          
# ==============
class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Aplicativo de Recomendação de Livros")
        self.geometry("645x280")
        self.resizable(False, False)

        self.frame_recomendador = RecomendadorLivrosView(controller.recomendador_controller)
        self.frame_recomendador.pack()
        controller.recomendador_controller.view = self.frame_recomendador