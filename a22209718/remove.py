# bands_musica

from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("DROP TABLE bands_musica;")