import json
from typing import List, Tuple
from collections import Counter
from multiprocessing import Pool, cpu_count


def process_chunk_q3(lines: List[str]) -> Counter:
    """
    Procesa un bloque de líneas y devuelve un Counter
    con el conteo de menciones por username.
    """
    counter = Counter()

    for line in lines:
        mentioned_users = json.loads(line).get("mentionedUsers")

        if not mentioned_users:
            continue

        counter.update(
            user["username"] for user in mentioned_users
        )

    return counter


def q3_time(file_path: str, chunk_size: int = 10_000) -> List[Tuple[str, int]]:
    """
    Q3 (versión paralela):

    Obtiene el top 10 histórico de usuarios más influyentes,
    medido por el número total de menciones (@) recibidas.

    - Divide el archivo en bloques (chunks)
    - Procesa cada bloque en paralelo
    - Reduce los contadores parciales
    """

    final_counter = Counter()
    chunks: List[List[str]] = []

    # 1. Leer archivo y dividir en chunks
    with open(file_path, "r", encoding="utf-8") as file:
        current_chunk = []

        for line in file:
            current_chunk.append(line)

            if len(current_chunk) >= chunk_size:
                chunks.append(current_chunk)
                current_chunk = []

        if current_chunk:
            chunks.append(current_chunk)

    # 2. Procesar chunks en paralelo
    with Pool(processes=cpu_count()) as pool:
        for partial_counter in pool.map(process_chunk_q3, chunks):
            final_counter += partial_counter

    # 3. Retornar top 10 usuarios más mencionados
    return final_counter.most_common(10)


if __name__ == "__main__":
    # Ejemplo de uso
    file_path = "tweets.json"
    result = q3(file_path)
    print(result)
