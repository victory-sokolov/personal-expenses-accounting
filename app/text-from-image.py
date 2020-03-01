import os

import cv2
import pytesseract
from PIL import Image

name = "rec.jpg"
image_folder = "input-receipt/original"
output_dir = "output-receipt"
filename = "{}.png".format(os.getpid())
lang="lav"

image = cv2.imread(f'{image_folder}/{name}')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename), config=f'--psm 6 -l {lang}')
print(text)

file = open("data-result.txt", "w")
file.write(text)
#os.remove(filename)
