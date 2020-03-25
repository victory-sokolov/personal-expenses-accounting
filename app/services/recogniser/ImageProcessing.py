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
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        median = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(
            median, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
        )[1]
        cv2.imwrite('output.png', thresh)


    def run_pipeline(self, image):
        return [
            self.change_image_DPI(image),
            self.binarize_image(image)
        ]

