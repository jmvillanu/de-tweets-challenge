import json
from typing import List, Tuple
from collections import Counter
from emoji import emoji_list


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            content = json.loads(line)["content"]
            emoji_counter.update(
                e["emoji"] for e in emoji_list(content)
            )

    return emoji_counter.most_common(10)


