# Importando os pacotes e bibliotecas 
import tkinter as tk # Pacote para criação de interface gráfica

# ===================
#      CONTROLLER     
# ===================
class RecomendadorLivrosController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def listar_livros(self):
        return self.model.obter_livros()
    
    def listar_recomendados(self, titulo):
        return self.model.obter_recomendados(titulo)
    
    def atualizar_recomendados(self, titulo):
        lista = self.model.obter_recomendados(titulo)
        self.view.atualizar_listbox(lista)
        
    def limpar_listbox(self):
        self.view.listbox_recomendados.delete(0, tk.END)