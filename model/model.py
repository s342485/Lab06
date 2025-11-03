from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self._automobili = [] #lista di tutte le auto nel database

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        if len(self._automobili) == 0:   #se non ancora letto dal database
            cnx = get_connection()
            cursor = cnx.cursor(dictionary = True)
            query = "SELECT * FROM automobile"   #dalla tabella automobile
            cursor.execute(query)
            result = cursor.fetchall() #prende tutte le righe

            for row in result:
                auto = Automobile(
                    row["codice"],
                    row["marca"],
                    row["modello"],
                    int(row["anno"]),
                    int(row["posti"]),
                    bool(row["disponibile"])
                )
                self._automobili.append(auto)

            cursor.close()
            cnx.close()

            return self._automobili


    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        cnx = get_connection()
        cursor = cnx.cursor(dictionary = True)

        query = "SELECT * FROM automobile WHERE LOWER(modello) LIKE LOWER(%s)"
        cursor.execute(query, (modello,))

        result = cursor.fetchall() #prende tutte le righe


        automobili_trovate = [] #lista locale
        for row in result:
            auto = Automobile(
                row["codice"],
                row["marca"],
                row["modello"],
                int(row["anno"]),
                int(row["posti"]),
                bool(row["disponibile"])
            )
            automobili_trovate.append(auto)

        cursor.close()
        cnx.close()

        return automobili_trovate


