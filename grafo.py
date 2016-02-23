"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067
implementacao de grafo - Data Structure
IFRN - Natal/RN - Brazil
2016
Contact: victor.limeira@outlook.com
"""
from __future__ import print_function

class VerticeExiste(Exception):
    pass


class ArestaExiste(Exception):
    pass


class Grafo():
    def __init__(self, vertice=None):
        self.vertices = []
        self.arestas = []
        if vertice is not None:
            self.inserir_vertice(vertice)

    def inserir_vertice(self, valor):
        """ Inserir um vertice com valor no grafo """

        novo_vertice = Vertice(valor)

        if not self.vertices:
            self.vertices.append(novo_vertice)
        else:
            for vertice in self.vertices:
                if vertice.valor is valor:
                    raise VerticeExiste()
            self.vertices.append(novo_vertice)

    def inserir_aresta(self, valor, saida, entrada):
        """ Inserir um vertice com valor no grafo direcionado """

        nova_aresta = Aresta(valor, saida, entrada)

        if self.arestas:
            for aresta in self.arestas:
                if [aresta.valor, aresta.saida, aresta.entrada] == [
                        valor, saida, entrada]:
                    raise ArestaExiste()
            self.arestas.append(nova_aresta)
        else:
            self.arestas.append(nova_aresta)

    def mostrar_vertices(self):
        """ Mostrar todos os valores dos vertices inseridos """

        valores = []
        for vertice in self.vertices:
            valores.append(vertice.valor)
        print(valores)

    def mostrar_arestas(self):
        """ Mostrar todos os valores das arestas inseridas """

        valores = []
        for aresta in self.arestas:
            valores.append([aresta.valor, aresta.saida, aresta.entrada])
        print(valores)

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


class Aresta():
    def __init__(self, valor, saida, entrada):
        self.valor = valor
        self.saida = saida
        self.entrada = entrada
