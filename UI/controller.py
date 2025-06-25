import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDAnno(self):
        years = self._model.getYears()
        self._view.ddyear.options.clear()
        for y in years:
            self._view.ddyear.options.append(ft.dropdown.Option(y))
        self._view.update_page()

    def fillDDStati(self,e):
        year=self._view.ddyear.value
        self._view.ddstate.options.clear()
        self._view.ddstate.value=None
        states = self._model.getStates(year)
        for s in states:
            self._view.ddstate.options.append(ft.dropdown.Option(key=s.id, text=s.name))
        self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result1.controls.clear()
        anno=self._view.ddyear.value
        stato=self._view.ddstate.value
        self._model.buildGraph(anno,stato)
        self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {self._model.getNumEdges()}"))
        self._view.txt_result1.controls.append(ft.Text(f"Il grafo ha: {self._model.getCompConn()} componenti connesse"))
        self._view.txt_result1.controls.append(ft.Text(f"La componente connessa più grande è costituita da {len(self._model.getCompConnMax())} nodi"))
        for nodo in self._model.getCompConnMax():
            self._view.txt_result1.controls.append(ft.Text(nodo))
        self._view.update_page()

    def handle_path(self, e):
        pass

