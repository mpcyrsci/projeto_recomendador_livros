# Recomendador de Livros

Aplicação em **Python** que recomenda livros semelhantes com base em um título escolhido pelo usuário.  
O sistema utiliza **Machine Learning (KNN)** e uma interface gráfica feita com **Tkinter**.

## Funcionalidades
- Seleção de um livro em uma lista interativa.  
- Exibição de livros recomendados com base em similaridade.  
- Interface simples e intuitiva.  
- Carregamento de dados a partir de arquivo.  

## Tecnologias Utilizadas
- **Python 3.13.5**  
- **Tkinter** – interface gráfica  
- **pandas**, **numpy**, **scikit-learn** – processamento e treinamento do modelo KNN  
- **pickle** – salvamento e carregamento do modelo e do dataframe com as informações dos livros

## Funcionamento

O sistema utiliza o algoritmo **K-Vizinhos Mais Próximos (KNN)** para identificar livros semelhantes com base em seus padrões de avaliação. Primeiro, é construída uma **tabela pivô**, onde cada linha representa um livro e cada coluna representa um usuário (ou característica associada).  
Em seguida, o **modelo KNN** é treinado sobre essa estrutura para aprender as **relações de similaridade** entre os livros. Quando o usuário escolhe um título e clica em **“Recomendar”**, o modelo retorna os livros mais próximos em termos de similaridade.

---

Projeto desenvolvido para estudo de POO, MVC e Sistemas de Recomendação utilizando o modelo KNN em Python.
