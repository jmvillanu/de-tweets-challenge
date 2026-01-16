import json
from typing import List, Tuple
from datetime import datetime

def q1(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Procesa un archivo de tweets en formato JSON y obtiene una
    lista de tuplas con las 10 fechas con mayor número de tweets y el
    username del usuario que tuvo más tweets en la fecha respectiva.

    El archivo debe contener un tweet por línea en formato JSON, con al menos
    los siguientes campos:
    - 'date': Fecha y hora del tweet en formato ISO (Ejemplo: "2010-04-28T03:12:18+00:00")
    - 'username': Nombre de usuario que publicó el tweet. En este caso está anidado en
    'user'.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[datetime.date, str]]:
        Una lista de tuplas donde cada elemento contiene:
        - La fecha, en formato: datetime.date
        - El nombre del usuario con mayor número de tweets en esa fecha

        Solo se retorna el top 10 de fechas con más tweets y el username respectivo.
    """
    
    with open(file_path, 'r', encoding='utf-8') as file:
        
        # Diccionario con el conteo de tweets por fecha
        # {datetime.date: tweets_count}
        tweet_dates_count = {}
        
        # Diccionario con el conteo de tweets por username y fecha
        # {datetime.date: {username: tweets_count}}
        tweet_dates_list = {}
        
        for line in file:
            
            tweet = json.loads(line)
            tweet_date = datetime.fromisoformat(tweet['date']).date()
            username = tweet['user']['username']
            
            # Si la fecha está en tweet_dates_count, suma 1.
            if tweet_date in tweet_dates_count:
                tweet_dates_count[tweet_date] += 1
            else:
                # Si la fecha NO está en tweet_dates_count, inicia el conteo en 1.
                tweet_dates_count[tweet_date] = 1
                # Si la fecha NO está en tweet_dates_list, agrega al diccionario
                # la fecha como llave (key) y valor un diccionario vacío.
                tweet_dates_list[tweet_date] = {}
                
            # Conteo de tweets por username en cada fecha.
            # Misma lógica que lo anterior, si no está, inicia en 1.
            # Si sí está, suma 1.
            if username in tweet_dates_list[tweet_date]:
                tweet_dates_list[tweet_date][username] += 1
            else:
                tweet_dates_list[tweet_date][username] = 1
        
    # Obtener las 10 fechas con mayor número de tweets
    top_10_dates = sorted(
        tweet_dates_count,
        key=tweet_dates_count.get,
        reverse=True
    )[:10]

    result = []

    # Para cada una de las fechas top 10,
    # obtiene el usuario con mayor número de tweets
    for tweet_date in top_10_dates:
        usernames_dict = tweet_dates_list[tweet_date]
        top_username = max(usernames_dict, key=usernames_dict.get)
        result.append((tweet_date, top_username))

    return result
