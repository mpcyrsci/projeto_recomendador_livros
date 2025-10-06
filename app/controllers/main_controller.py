import tkinter as tk
from app.views.main_view import MainView
from app.models.recomendador_model import RecomendadorLivros
from app.views.recomendador_view import RecomendadorLivrosView
from app.controllers.recomendador_controller import RecomendadorLivrosController

# ===================
#      CONTROLER     
# ===================
class MainController:
    def __init__(self, modelo_path, livros_path):
        self.model = RecomendadorLivros(modelo_path, livros_path)
        self.recomendador_controller = RecomendadorLivrosController(self.model, None)
        self.view = MainView(self)

    def abrir_recomendador(self):
        # Cria a View do Recomendador passando o controller do recomendador
        top = tk.Toplevel(self.view)
        recomendador_view = RecomendadorLivrosView(self.recomendador_controller, master=top)
        recomendador_view.pack()
        self.recomendador_controller.view = recomendador_view

    def run(self):
        self.view.mainloop()