from functools import reduce
from time import sleep

import cv2
import numpy as np
from wand.image import Image as WandImage

from base.ProcessManager import ProcessManager


class ImageProcessing:

    def __init__(self, image):
        self.image_name = image
        self.image = cv2.imread(image)

    def change_image_DPI(self, image):
        process_params = [
            "mogrify", "-set", "density", "300", image
        ]
        process = ProcessManager.create_process(process_params)

    def rotate(self, image):
        angle = 90
        (h, w) = image.shape[:2]
        if h < w:
            with WandImage(filename=self.image_name) as img:
                img.rotate(angle)
                img_buffer = np.asarray(
                    bytearray(img.make_blob()), dtype=np.uint8)

            if img_buffer is not None:
                retval = cv2.imdecode(img_buffer, cv2.IMREAD_UNCHANGED)
                return retval
        else:
            return self.image

    def gray_scale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def noise_removal(self, image):
        return cv2.GaussianBlur(image, (5, 5), 0)

    def thresh(self, image):
        return cv2.threshold(
            image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
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
        # self.rotate(self.image)

        return reduce(
            lambda image, function: function(image), (
                self.rotate,
                self.gray_scale,
                self.noise_removal,
                self.thresh,
                self.save_image
            ),
            self.image
        )
