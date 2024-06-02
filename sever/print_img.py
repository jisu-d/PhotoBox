import cv2
import win32print
import win32ui
from PIL import Image, ImageWin

def print_image(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
    
    # 이미지 크기 설정 (100 x 148 mm)
    target_width_mm = 100.0
    target_height_mm = 148.0
    
    # mm 단위를 픽셀로 변환 (프린터의 해상도를 300 DPI로 가정)
    dpi = 300
    target_width_px = int(target_width_mm * dpi / 25.4)
    target_height_px = int(target_height_mm * dpi / 25.4)
    
    # 이미지 크기 조정
    resized_image = cv2.resize(image, (target_width_px, target_height_px))
    
    # 프린터 설정 가져오기
    printer_name = 'Canon SELPHY CP1300'
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)
    
    # 프린터 해상도 가져오기
    printable_area = hdc.GetDeviceCaps(8), hdc.GetDeviceCaps(10)
    
    # 프린트 영역의 중심 좌표 계산
    center_x = printable_area[0] // 2
    center_y = printable_area[1] // 2
    
    # 이미지를 중심으로 이동시키기 위한 좌표 계산
    start_x = center_x - (target_width_px // 2)
    start_y = center_y - (target_height_px // 2)
    end_x = start_x + target_width_px
    end_y = start_y + target_height_px
    
    # 출력 영역 설정
    hdc.StartDoc(image_path)
    hdc.StartPage()
    
    # OpenCV 이미지 -> Pillow 이미지로 변환
    resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(resized_image)
    dib = ImageWin.Dib(pil_image)
    
    # 이미지를 중심으로 이동시키면서 그리기
    dib.draw(hdc.GetHandleOutput(), (start_x, start_y, end_x, end_y))
    
    # hdc.EndPage()
    # hdc.EndDoc()
    # hdc.DeleteDC()

    cv2.imshow('Result', dib)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 인쇄할 이미지 경로 설정
    image_path = "C:/Users/lim16/Desktop/PhotoBox/sever/29-F683C.jpg"
    print_image(image_path)
