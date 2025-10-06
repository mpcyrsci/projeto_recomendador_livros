from app.controllers.main_controller import MainController

if __name__ == "__main__":
    modelo_path = "data/processed/modelo_knn.pkl"
    livros_path = "data/processed/livros_pivot.pkl"

    app = MainController(modelo_path, livros_path)
    app.run()