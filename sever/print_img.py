import subprocess
def printImgs(printoutNum, path):
    for _ in range(printoutNum):
        subprocess.run(['lp', '-d', 'Canon_SELPHY_CP1300_', f'/home/jisu/project/PhotoBox/sever/save/{path}.jpg'], check=True)


# import cv2
# import subprocess

# def crop_image(image_path, output_path, dpi=300, crop_mm=50):
#     # Convert mm to pixels
#     crop_px = int(dpi * (crop_mm / 25.4))

#     # Load the image
#     image = cv2.imread(image_path)

#     # Get the dimensions of the original image
#     height, width, channels = image.shape

#     # Calculate the new dimensions
#     new_width = width - crop_px
#     new_height = height - crop_px


#     # Crop the image
#     cropped_image = image[:new_height, :new_width]

#     # Save the cropped image
#     cv2.imwrite(output_path, cropped_image)

# def printImgs(printoutNum, path):
#     image_path = f'/home/jisu/project/PhotoBox/sever/save/{path}.jpg'
#     output_path = f'/home/jisu/project/PhotoBox/sever/save/{path}_cropped.jpg'
    
#     # Crop the image
#     crop_image(image_path, output_path)
    
#     # Print the cropped image
#     for _ in range(printoutNum):
#         subprocess.run(['lp', '-d', 'Canon_SELPHY_CP1300_', output_path], check=True)


