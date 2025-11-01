from database.DB_connect import get_connection
from model.noleggio import Noleggio


class NoleggioModel:
    def __init__(self):
        self.DB_connect = get_connection()

    def get_noleggi(self):
        conn = self.DB_connect.get_connection()
        cursor = conn.cursor()
        query = """SELECT * FROM noleggio"""
        cursor.execute(query)
        noleggi = []
        for row in cursor:
            noleggio = Noleggio(row[0], row[1], row[2], row[3])
            noleggi.append(noleggio)
        cursor.close()
        conn.close()
        return noleggi

