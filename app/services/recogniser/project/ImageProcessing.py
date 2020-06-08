from functools import reduce
from time import sleep

import cv2
import numpy as np
from wand.image import Image as WandImage

from app.base.ProcessManager import ProcessManager


class ImageProcessing:

    def __init__(self, image):
        self.image_path = image
        self.image_name = image.split("/")[-1]
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
            with WandImage(filename=self.image_path) as img:
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
            image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

    def adaptive_thresh(self, image):
        return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 121, 12)

    def save_image(self, image):
        cv2.imwrite('recogniser/project/output.png', image)

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

    def dilate(self, image):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.dilate(image, kernel, iterations=1)

    def erode(self, image):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.erode(image, kernel, iterations=1)

    def cut_image(self, image):
        """ Cut edges of receipt image"""
        image_resized = cv2.resize(image, (800, 800))
        blurred = cv2.GaussianBlur(image_resized, (5, 5), 0)
        edge = cv2.Canny(blurred, 70, 200)
        contours, hierarchy = cv2.findContours(
            edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        for contour in contours:
            sq = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02*sq, True)

            if len(approx) == 4:
                target = approx
                break

        # approx = mapper.mapp(target)  # find endpoints of the sheet
        pts = np.float32([[0, 0], [800, 0], [800, 800], [0, 800]])

        op = cv2.getPerspectiveTransform(approx, pts)
        dst = cv2.warpPerspective(image, op, (800, 800))
        return dst

    def run_pipeline(self):
        rotated_image = self.rotate(self.image)
        cv2.imwrite(
            f'recogniser/project/receipts/{self.image_name}', rotated_image
        )
        self.image = rotated_image
        # Temp code: move image to assets folder
        import shutil
        import os
        from os.path import expanduser
        home = expanduser("~")
        shutil.move(f'{os.getcwd()}/recogniser/project/receipts/{self.image_name}',
                    f'{home}/Documents/personal-expenses-accounting/app/services/client/public/images/receipts')
        # code end
        return reduce(
            lambda image, function: function(image), (
                self.gray_scale,
                self.thresh,
                self.noise_removal,
                self.save_image
            ),
            self.image
        )
