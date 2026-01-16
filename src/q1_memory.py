import json
from typing import List, Tuple
from datetime import datetime, date
from collections import Counter, defaultdict


def q1_memory(file_path: str) -> List[Tuple[date, str]]:
    """
    Q1 (versión senior)

    - Identifica las 10 fechas con mayor número de tweets
    - Para cada fecha, obtiene el usuario más activo
    - Optimizada para archivos grandes (lectura en streaming)
    """

    # Conteo total de tweets por fecha
    tweets_count: Counter[date] = Counter()

    # Conteo de tweets por usuario dentro de cada fecha
    username_per_date: defaultdict[date, Counter[str]] = defaultdict(Counter)

    # 1. Procesamiento en streaming (O(n), memoria controlada)
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            tweet = json.loads(line)

            date_ = tweet['date'][0:10]
            usuario = tweet["user"]["username"]

            tweets_count[date_] += 1
            username_per_date[date_][usuario] += 1

    # 2. Top 10 fechas con más tweets (O(d log 10))
    top_10_dates = tweets_count.most_common(10)

    # 3. Usuario más activo por cada fecha (O(u) por fecha)
    return [
        (
            date_,
            username_per_date[date_].most_common(1)[0][0]
        )
        for date_, _ in top_10_dates
    ]
