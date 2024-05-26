import cv2

def print_collage_imges(data):
    imges_path = data.imges_path
    print_num = data.print_num

    image = cv2.imread(f'C:\Users\lim16\Desktop\PhotoBox\sever\save/{imges_path}.jpg')

