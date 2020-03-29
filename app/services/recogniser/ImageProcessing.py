from functools import reduce

import cv2
import numpy as np
from base.ProcessManager import ProcessManager


class ImageProcessing:

    def __init__(self, image):
        self.change_image_DPI(image)
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

    def deskew(self, image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(
            image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    def run_pipeline(self):

        return reduce(
            lambda image, function: function(image), (
                self.gray_scale,
                self.noise_removal,
                self.binarize_image,
                self.deskew,
                self.save_image
            ),
            self.image
        )


ImageProcessing("IMG_20200215_234244.jpg").run_pipeline()
