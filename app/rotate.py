import os

import cv2


def read_images_from_folder():
  images = []
  folder = 'input-receipt/original'

  for file in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, file))
    if img is not None:
      images.append(file)
  return images


def rotate():
  img_directory = "input-receipt"
  angle = 90
  images = read_images_from_folder()

  for img in images:
    image = cv2.imread(f'{img_directory}/original/{img}')
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)

    if h > w:
      #print(img)
      rotate_val = cv2.getRotationMatrix2D(center, angle, 0.9)
      # apply rotation to the image
      output = cv2.warpAffine(image, rotate_val, (w, h))
      cv2.imwrite(f'{img_directory}/original/{img}', output)


rotate()
