from typing import List, Tuple
import json
from collections import Counter
from emoji import emoji_list


def q2(file_path: str) -> List[Tuple[str, int]]:
    """
    Optimizada en memoria:
    - Procesamiento en streaming
    - No se crean listas intermedias
    - Solo se mantienen contadores
    """

    emoji_counter = Counter()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            content = json.loads(line)["content"]

            # Generador → cero listas temporales
            for e in emoji_list(content):
                emoji_counter[e["emoji"]] += 1

    return emoji_counter.most_common(10)