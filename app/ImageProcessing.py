import cv2
import numpy as np
from PIL import Image

from app.services.tesseract.ProcessManager import ProcessManager


class ImageProcessing:

    def change_image_DPI(self, image):
        process_params = [
            "mogrify", "-set", "density", "300", image
        ]
        process = ProcessManager.create_process(process_params)

    def binarize_image(self, image):
        img = cv2.imread(image)
        kernel = np.ones((5, 5), np.uint8)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        median = cv2.medianBlur(gray, 5)
        thresh = cv2.threshold(
            median, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        #dilatate = cv2.dilate(thresh, kernel, iterations=1)
        img_erosion = cv2.erode(thresh, kernel, iterations=1)
        cv2.imwrite('output.png', img_erosion)
