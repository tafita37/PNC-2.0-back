from django.db import connection

def getAllEntitePaginate(pageNumber):
    # Exécuter une requête SQL brute avec LIMIT
    sql_query = "SELECT * FROM entite LIMIT 20 OFFSET %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query, [(pageNumber-1)*20])
        rows = cursor.fetchall()

    return rows