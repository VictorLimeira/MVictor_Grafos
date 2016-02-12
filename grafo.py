"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067
implementacao de grafo - Data Structure
IFRN - Natal/RN - Brazil
2016
Contact: victor.limeira@outlook.com
"""


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

        if not self.arestas:
            self.arestas.append(nova_aresta)
        else:
            for aresta in self.arestas:
                if [aresta.valor, aresta.saida, aresta.entrada] == [
                        valor, saida, entrada]:
                    raise ArestaExiste()
            self.arestas.append(nova_aresta)

    def mostrar_vertices(self):
        """ Mostrar todos os valores dos vertices inseridos """

        valores = []
        for vertice in self.vertices:
            valores.append(vertice.valor)
        print valores


class Vertice():
    def __init__(self, valor):
        self.valor = valor


class Aresta():
    def __init__(self, valor, saida, entrada):
        self.valor = valor
        self.saida = saida
        self.entrada = entrada
