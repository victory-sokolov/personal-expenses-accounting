from functools import reduce
import cv2
import numpy as np
from PIL import Image
#from app.services.tesseract.ProcessManager import ProcessManager


class ImageProcessing:

    def __init__(self, image):
        self.image = cv2.imread(image)

    def change_image_DPI(self, image):
        process_params = [
            "mogrify", "-set", "density", "300", image
        ]
        process = ProcessManager.create_process(process_params)

    def gray_scale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def noise_removal(self, image):
        return cv2.GaussianBlur(image, (5, 5), 0)

    def binarize_image(self, image):
        return cv2.threshold(
            image, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
        )[1]

    def save_image(self, image):
        cv2.imwrite('output.png', image)


    def run_pipeline(self):
        #self.change_image_DPI(self.image)
        return reduce(
            lambda image, function: function(image), (
                self.gray_scale,
                self.noise_removal,
                self.binarize_image,
                self.save_image
            ),
            self.image
        )
