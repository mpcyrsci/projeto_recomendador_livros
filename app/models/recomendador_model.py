import joblib

# ===============
#      MODEL               
# ===============
class RecomendadorLivros:
    def __init__(self, modelo_path, livros_path):
        self.__modelo = joblib.load(modelo_path)
        self.__livros_pivot = joblib.load(livros_path)
        self.__livros = []
        self.__livros_recomendados = []

    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def livros_pivot(self):
        return self.__livros_pivot
    
    @property
    def livros(self):
        return self.__livros
    
    @property
    def livros_recomendados(self):
        return self.__livros_recomendados
    
    def obter_livros(self):
        self.__livros = self.livros_pivot.index.tolist()
        return self.__livros
    
    def obter_recomendados(self, titulo_livro):
        self.__livros_recomendados = []
        linha = self.__livros_pivot.loc[titulo_livro].values.reshape(1, -1)
        distances, suggestions = self.__modelo.kneighbors(linha)
        for i in suggestions[0][1:]:
            self.__livros_recomendados.append(self.__livros_pivot.index[i])
        return self.__livros_recomendados