import os
import random
from pathlib import Path


def get_random_img(data: list[str] | None = None) -> str:
    if data:
        return random.choice(data)
    return random.choice(_get_img_in_curdir())


def _get_img_in_curdir() -> list[str]:
    img = []
    for file in os.listdir():
        if Path(file).suffix == ".png":
            img.append(file)
    return img

print(get_random_img())