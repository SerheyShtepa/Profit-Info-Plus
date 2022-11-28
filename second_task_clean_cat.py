
from PIL import Image, ImageDraw
import numpy as np
from numpy import ndarray


def rectangle_variant_dictionary(arr: ndarray) -> dict:

    start_line = 0
    finish_line = 100
    domain = {}
    for column in range(len(arr) - 100):
        start_column = 0
        finish_column = 100
        for line in range(len(arr[0]) - 100):
            matrix = arr[start_line:finish_line, start_column:finish_column]
            domain[start_column, start_line] = np.sum(matrix)
            start_column += 1
            finish_column += 1
        start_line += 1
        finish_line += 1
    return domain


def outline_drawing(domain: dict, dark: bool = True):
    if dark:
        x, y = min(domain, key=domain.get)
    else:
        x, y = max(domain, key=domain.get)
    draw = ImageDraw.Draw(img, "RGBA")
    a = ["white" if dark  # selects the color of the square
         else "black"]
    draw.rectangle(xy=(x, y, x + 100, y + 100), outline=a[0])
    img.show()


if __name__ == "__main__":
    with Image.open("Profit-Info-Plus/katran-siniy.jpg") as img:
        img.load()
        arr = np.asarray(img.convert("L"))
        outline_drawing(rectangle_variant_dictionary(arr))


