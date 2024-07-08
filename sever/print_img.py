# import cv2
# import numpy as np
# import subprocess

# image = cv2.imread('/home/jisu/project/PhotoBox/sever/29-F683C.jpg')

# width_mm = 100
# height_mm = 148
# dpi = 300
# width_px = int(width_mm / 25.4 * dpi)
# height_px = int(height_mm / 25.4 * dpi)

# resized_image = cv2.resize(image, (width_px, height_px))

# cv2.imwrite('/home/jisu/project/PhotoBox/sever/processed_image', resized_image)

# subprocess.run(['lp', '-d', 'Canon_SELPHY_CP1300', '-o', 'media=Custom.100x148mm', '/home/jisu/project/PhotoBox/sever/processed_image.jpg'])

import subprocess
def printImgs(printoutNum, path):
    for _ in range(printoutNum):
        subprocess.run(['lp', '-d', 'Canon_SELPHY_CP1300_', f'/home/jisu/project/PhotoBox/sever/save/{path}.jpg'], check=True)


