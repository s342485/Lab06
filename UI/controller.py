import flet as ft
from flet.core import page

from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, model : Autonoleggio, view : View):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    def handler_mostra_automobili(self,e):
        lista_auto_view = self._view.lista_auto #me la prendo dalla view
        try:
            automobili = self._model.get_automobili()

            lista_auto_view.controls.clear() #pulisce la lista
            if not automobili:
                lista_auto_view.controls.append(ft.Text("Nessuna automobile trovata"))
            else:
                for auto in automobili:
                    stato = "✅" if getattr(auto, "disponibile", True) else "⛔"
                    lista_auto_view.controls.append(ft.Text(f"{stato} {auto}"))

                self._view.update()
        except Exception as e:
            self._view.show_alert(f"Errore nel caricamento delle automobili: {e}")


    def handler_ricerca_per_modello(self,e, modello):
        lista_auto_per_modello = self._view.lista_auto_ricerca

        #inserisco un caricamento!
        lista_auto_per_modello.controls.clear()
        lista_auto_per_modello.controls.append(ft.Text("⏳ Caricamento in corso..."))
        self._view.update()

        try:
            auto_filtrate = self._model.cerca_automobili_per_modello(modello)

            if not auto_filtrate:
                lista_auto_per_modello.controls.append(ft.Text("Nessuna automobile trovata"))
            else:
                for auto in auto_filtrate:
                    stato = "✅" if getattr(auto, "disponibile", True) else "⛔"
                    lista_auto_per_modello.controls.append(ft.Text(f"{stato} {auto}"))

        except Exception as e:
            self._view.show_alert(f"Errore nel caricamento delle automobili: {e}")

        self._view.update()







