from database.DB_connect import get_connection
from model.automobile import Automobile


class AutomobileDAO:
    def __init__(self):
        self.conn = get_connection() #inizia la connessione

    def get_automobili(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM automobile"
        cursor.execute(query)
        automobili = []
        for row in cursor:
            auto = Automobile(row[0], row[1], row[2], row[3], row[4], row[5])
            automobili.append(auto)
        cursor.close()
        return automobili
