import json
from typing import List, Tuple
from collections import Counter
from multiprocessing import Pool, cpu_count
from emoji import emoji_list


def process_chunk(lines: list[str]) -> Counter:
    """
    Procesa un bloque de líneas y devuelve un Counter
    con el conteo de emojis en ese bloque.
    """
    counter = Counter()

    for line in lines:
        content = json.loads(line)["content"]
        counter.update(e["emoji"] for e in emoji_list(content))

    return counter


def q2_time(file_path: str, chunk_size: int = 10_000) -> List[Tuple[str, int]]:
    """
    Q2 (versión paralela)

    - Divide el archivo en bloques (chunks)
    - Procesa cada bloque en paralelo
    - Combina los resultados parciales
    - Devuelve los 10 emojis más usados con su conteo total
    """

    final_counter = Counter()
    chunks: list[list[str]] = []

    # 1. Leer el archivo y dividirlo en chunks
    with open(file_path, "r", encoding="utf-8") as file:
        current_chunk = []

        for line in file:
            current_chunk.append(line)

            if len(current_chunk) >= chunk_size:
                chunks.append(current_chunk)
                current_chunk = []

        if current_chunk:
            chunks.append(current_chunk)

    # 2. Procesar los chunks en paralelo
    with Pool(processes=cpu_count()) as pool:
        for partial_counter in pool.map(process_chunk, chunks):
            final_counter += partial_counter

    # 3. Top 10 emojis más usados
    return final_counter.most_common(10)