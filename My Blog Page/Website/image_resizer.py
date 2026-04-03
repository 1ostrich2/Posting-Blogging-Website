# COPY PASTED FROM A DIFFRENT PROJECT OF MINE, AND THEN SLIGHTLY MODIFIED TO SUIT THIS

import PIL
from PIL import Image
import io


def image_resizer():
    buffered = io.BytesIO()

    while True:
        file_format = str(input("file format: "))
        s = str(input("file name: "))

        img = Image.open(f'Website/static/ui/{s}.{file_format}')
        img.thumbnail([30,30], PIL.Image.ANTIALIAS)
        img.save(f"Website/static/ui/{s}.{file_format}", format=f"{file_format}")

image_resizer()
