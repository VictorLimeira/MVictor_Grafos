"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067
implementacao de grafo - Data Structure
IFRN - Natal/RN - Brazil
2016
Contact: victor.limeira@outlook.com
"""
from __future__ import print_function

class VerticeExisteError(Exception):
    pass


class ArestaExisteError(Exception):
    pass


class Grafo():
    def __init__(self):
        self.vertices = []

    def inserir_vertice(self, valor):
        """ Inserir um vertice com valor no grafo """
        for vertice in self.vertices:
            if vertice.valor is valor:
                raise VerticeExisteError

        vertice = Vertice(valor)
        self.vertices.append(vertice)
        return None

    def inserir_aresta(self, valor, saida, entrada):
        """ Inserir um vertice com valor no grafo direcionado """
        vertice_saida = self.get_vertice(saida)
        vertice_entrada = self.get_vertice(entrada)

        
        pass

    def get_vertice(self, valor):
        for vertice in self.vertices:
            if vertice.valor is valor:
                return vertice
        return None

    def mostrar_vertices(self):
        """ Mostrar todos os valores dos vertices inseridos """
        pass

    def mostrar_arestas(self):
        """ Mostrar todos os valores das arestas inseridas """
        pass

    def matriz_adjacencia(self):
        """ Mostra a matriz de adjacencia do Grafo """
        # Primeira linha
        print("   ", end="")
        for vertice in self.vertices:
            print(" " + str(vertice.valor) + " ", end="")
        print("")
        # Fim primeira linha

        encontrado = False
        for vertice in self.vertices:
            # Inicio de cada linha
            print(" " + str(vertice.valor) + " ", end="") # Imprime o valor do vertice atual na horizontal
            # Comparacao de cada outro vertice com o atual
            for vertice2 in self.vertices:
                # Varredura das arestas
                for aresta in self.arestas:
                    valores = [aresta.saida, aresta.entrada]
                    # Encontrar se existe aresta para os dois vertices
                    if ((vertice.valor is valores[0]) and (vertice2.valor is valores[1])
                        ) or ((vertice.valor is valores[1]) and (vertice2.valor is valores[0])): # Aresta encontrada
                        print(" " + str(1) + " ", end="")
                        encontrado = True
                # Apos a verradura de todas as arestas, se nao foi encontrado, colocar 0.
                if encontrado is not True:
                    print(" " + str(0) + " ", end="")
                else:
                    encontrado = False
            print("") # Fim de cada linha



class Vertice():
    def __init__(self, valor):
        self.valor = valor
        self.arestas = []

    def add_aresta(self, valor, entrada):
        aresta = Aresta(valor, entrada)
        self.arestas.append(Aresta)
        return None

class Aresta():
    def __init__(self, valor, entrada):
        self.valor = valor
        self.entrada = entrada
