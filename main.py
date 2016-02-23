"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067
implementacao de grafo - Data Structure
IFRN - Natal/RN - Brazil
2016
Contact: victor.limeira@outlook.com
"""
from grafo import *

if __name__ == '__main__':

    # Popular o grafo
    meu_grafo = Grafo(2) # Inicia o grafo já com o vertice 2
    meu_grafo.inserir_vertice(3)
    meu_grafo.inserir_vertice(4)
    meu_grafo.inserir_vertice(5)
    meu_grafo.inserir_aresta(3, 2, 3)
    meu_grafo.inserir_aresta(4, 4, 2)
    meu_grafo.inserir_aresta(8, 5, 4)

    # Imprimir matriz de adjacencia
    meu_grafo.matriz_adjacencia()
