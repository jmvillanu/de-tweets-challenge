from typing import List, Tuple
import json
from collections import Counter


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Q3:
    Obtiene el top 10 histórico de usuarios más influyentes,
    medido por el número total de menciones (@) recibidas.
    """

    users_counter = Counter()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            mentioned_users = json.loads(line).get("mentionedUsers")

            # Si no hay menciones, se continúa
            if not mentioned_users:
                continue

            # Se cuentan todas las menciones (puede haber varias por tweet)
            users_counter.update(
                user["username"] for user in mentioned_users
            )

    return users_counter.most_common(10)