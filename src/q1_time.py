import json
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Procesa un archivo de tweets en formato JSON y obtiene una
    lista de tuplas con las 10 fechas con mayor número de tweets y el
    username del usuario que tuvo más tweets en la fecha respectiva.

    El archivo debe contener un tweet por línea en formato JSON, con al menos
    los siguientes campos:
    - 'date': Fecha y hora del tweet en formato ISO (Ejemplo: "2010-04-28T03:12:18+00:00")
    - 'username': Nombre de usuario que publicó el tweet. En este caso está 
    anidado dentro del campo 'user'.

    La función optimiza el tiempo de ejecución utilizando estructuras de datos
    eficientes para el conteo y agregación de información.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[datetime.date, str]]:
        Una lista de tuplas donde cada elemento contiene:
        - La fecha, en formato: datetime.date
        - El nombre del usuario con mayor número de tweets en esa fecha

        Solo se retorna el top 10 de fechas con más tweets y el username
        correspondiente a cada una.
    """

    tweet_dates_count = Counter()
    tweet_dates_users = defaultdict(Counter)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            tweet_date = datetime.fromisoformat(tweet['date']).date()
            username = tweet['user']['username']

            tweet_dates_count[tweet_date] += 1
            tweet_dates_users[tweet_date][username] += 1

    top_10_dates = tweet_dates_count.most_common(10)

    return [
        (date, tweet_dates_users[date].most_common(1)[0][0])
        for date, _ in top_10_dates
    ]