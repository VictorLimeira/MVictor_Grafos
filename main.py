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

    meu_grafo = Grafo(2)
    meu_grafo.inserir_vertice(3)
    meu_grafo.mostrar_vertices()
    meu_grafo.inserir_aresta(3, 2, 3)
    meu_grafo.inserir_aresta(3, 2, 3)
