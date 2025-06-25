from networkx.classes import edges
from model.sighting import Sighting
from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.idMap={}
        self.grafo=nx.Graph()

    def getYears(self):
        return DAO.getYears()

    def getStates(self,year):
        return DAO.getStates(year)

    def buildGraph(self,anno,stato):
        self.grafo.clear()
        nodi=DAO.getAllNodi(anno,stato)
        for n in nodi:
            self.idMap[n.id]=n
        self.grafo.add_nodes_from(nodi)
        archi=DAO.getAllEdges(anno,stato,self.idMap)
        for arco in archi:
            if arco[0].distance_HV(arco[1])<100:
                self.grafo.add_edge(arco[0],arco[1])


    def getNumNodes(self):
        return len(list(self.grafo.nodes))

    def getNumEdges(self):
        return len(list(self.grafo.edges))

    def getCompConn(self):
        return nx.number_connected_components(self.grafo)

    def getCompConnMax(self):
        componenti=list(nx.connected_components(self.grafo))
        componenti.sort(key=lambda x: len(x),reverse=True)
        return componenti[0]
