import logging
from functools import reduce
from PIL import Image
import cv2
import numpy as np

class ImageProcessing:

    def __init__(self, image):
        self.image = image

    def rect_kernel(self):
        return cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    def resize_image(self, image):
        """Resize image.
        interpolation methods:
            * INTER_CUBIC
            * INTER_LINEAR
            * INTER_AREA
        Args:
            image (cv2): Image data

        Returns:
            cv2: Image data
        """
        return cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)


    def rotate(self, image):
        (h, w) = image.shape[:2]
        if h < w:
            return cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)

        return self.image

    def gray_scale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def avg_blur(self, image):
        return cv2.blur(image,(5,5))

    def gausian_blur(self, image):
        return cv2.GaussianBlur(image, (5, 5), 0)

    def media_blur(self, image):
        return cv2.medianBlur(image, 3)

    def bilateral_filter(self, image):
        return cv2.bilateralFilter(image,9,75,75)

    def thresh_otsu(self, image):
        return cv2.threshold(
            image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

    def thresh_binary(self, image):
        return cv2.threshold(image,127,255, cv2.THRESH_BINARY)

    def adaptive_thresh(self, image):
        return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 121, 12)

    def save_image(self, image):
        path = 'recognition/output.jpg'
        if isinstance(image, Image.Image):
            print("WRiting image")
            img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(path, img)
            return img

        cv2.imwrite(path, image)
        return image

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
        kernel = self.rect_kernel()
        return cv2.dilate(image, kernel, iterations=1)

    def erode(self, image):
        kernel = self.rect_kernel()
        return cv2.erode(image, kernel, iterations=1)

    def opening(self, image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    def canny(self,image):
        return cv2.Canny(image, 100, 200)

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


    def cv2_to_pil(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return Image.fromarray(img)

    def run_pipeline(self):
        logging.info("Pre processing image data...")
        return reduce(
            lambda image, function: function(image), (
                self.rotate,
                self.resize_image,
                self.gray_scale,
                self.gausian_blur,
                self.thresh_otsu,
                self.save_image,
                self.cv2_to_pil,
            ),
            self.image
        )
