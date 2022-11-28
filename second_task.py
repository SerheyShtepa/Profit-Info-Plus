"""2. Выделить в изображении самый темный/светлый участок, ограниченный квадратом 100 на 100 пикселей"""
import time

from PIL import Image, ImageDraw
import numpy as np


def loading_displaying_saving(filename: str = "katran-siniy.jpg", dark: bool = True):
    """
    Selects the darkest/lightest area in the image, limited by a square of 100 by 100 pixels, and displays the image
    """
    with Image.open(filename) as img:
        start_time = time.time()
        img.load()
        arr = np.asarray(img.convert("L"))
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
            # zero coordinates of min/max brightness:
        if dark:
            x, y = min(domain, key=domain.get)
        else:
            x, y = max(domain, key=domain.get)
        draw = ImageDraw.Draw(img, "RGBA")
        a = ["white" if dark  # selects the color of the square
             else "black"]
        draw.rectangle(xy=(x, y, x + 100, y + 100), outline=a[0])
        img.show()
        print(time.time() - start_time)


if __name__ == "__main__":
    loading_displaying_saving(dark=True)
