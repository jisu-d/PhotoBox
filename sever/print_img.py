# import subprocess
# def printImgs(printoutNum, path):
#     pass
#     # for _ in range(printoutNum):
#     #     subprocess.run(['lp', '-d', 'Canon_SELPHY_CP1300_', f'/home/jisu/project/PhotoBox/sever/save/{path}.jpg'], check=True)


import cv2
import numpy as np
import subprocess

def add_white_space(image_path, output_path, dpi=300, space_mm=0.5):
    # Convert mm to pixels
    space_px = int(dpi * (space_mm / 25.4))

    # Load the image
    image = cv2.imread(image_path)

    # Get the dimensions of the original image
    height, width, channels = image.shape

    # Create a new image with the extra space
    new_width = width + space_px
    new_height = height + space_px
    new_image = np.ones((new_height, new_width, channels), dtype=np.uint8) * 255  # White background

    # Place the original image in the top-left corner of the new image
    new_image[:height, :width] = image

    # Save the new image
    cv2.imwrite(output_path, new_image)

def printImgs(printoutNum, path):
    image_path = f'/home/jisu/project/PhotoBox/sever/save/{path}.jpg'
    output_path = f'/home/jisu/project/PhotoBox/sever/save/{path}_modified.jpg'
    
    # Add white space to the image
    add_white_space(image_path, output_path)
    
    # Print the modified image
    for _ in range(printoutNum):
        subprocess.run(['lp', '-d', 'Canon_SELPHY_CP1300_', output_path], check=True)

# Example usage
printImgs(5, 'example_image')
