from django.db import connection

def get_nb_pages(table_name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT get_nb_page(%s)", [table_name])
        nb_pages = cursor.fetchone()[0]  # Récupère le premier élément de la première ligne
    return nb_pages