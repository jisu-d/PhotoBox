import cv2
import numpy as np
import random
import os

# 변수 초기화
points = []
scaling_factor = 1.0

def click_event(event, x, y, flags, param):
    global points, scaling_factor
    if event == cv2.EVENT_LBUTTONDOWN:
        original_x = int(x / scaling_factor)
        original_y = int(y / scaling_factor)
        point = (original_x, original_y)
        
        # +/- 30 픽셀 내의 점 찾기
        remove_point = None
        for p in points:
            if abs(p[0] - point[0]) <= 30 and abs(p[1] - point[1]) <= 30:
                remove_point = p
                break
        
        if remove_point:
            points.remove(remove_point)
        else:
            points.append(point)
            
        print(f"Current points: {points}")
        redraw_image()

def redraw_image():
    global combined_background, points, resized_background, scaling_factor

    # 복사본 만들기
    display_image = resized_background.copy()

    for point in points:
        x = int(point[0] * scaling_factor)
        y = int(point[1] * scaling_factor)
        cv2.circle(display_image, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(display_image, f'{point}', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    # 결과 출력
    cv2.imshow('Result', display_image)

def count_files(directory):
    # 디렉토리 내 파일 목록 가져오기
    files = os.listdir(directory)
    
    # 파일 수 세기
    file_count = len(files)
    
    return file_count

def overlay_images(background_image_paths, overlay_image_path, save_directory):
    global combined_background, resized_background, scaling_factor

    # 오버레이할 이미지 읽기
    overlay = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)
    overlay_height, overlay_width = overlay.shape[:2]

    # 오버레이 이미지 크기에 맞춰 빈 배경 이미지 생성
    combined_background = np.zeros((overlay_height, overlay_width, 3), dtype=np.uint8)

    # 배경 이미지들을 합성
    for background_path, points_list in background_image_paths:
        # 배경 이미지 읽기
        background = cv2.imread(background_path)

        # 네 꼭짓점 좌표
        dst_points = np.array(points_list, dtype=np.float32)

        # 오버레이 이미지의 네 꼭짓점 좌표
        src_points = np.array([[0, 0], [overlay_width, 0], [overlay_width, overlay_height], [0, overlay_height]], dtype=np.float32)

        # 투영 변환 매트릭스 계산
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)

        # 이미지 변환
        warped_background = cv2.warpPerspective(background, matrix, (overlay_width, overlay_height))

        # 합성
        combined_background = cv2.addWeighted(combined_background, 1, warped_background, 1, 0)

    # 오버레이 이미지의 알파 채널 분리
    if overlay.shape[2] == 4:
        alpha_mask = overlay[:, :, 3] / 255.0
        overlay_rgb = overlay[:, :, :3]
    else:
        alpha_mask = np.ones((overlay.shape[0], overlay.shape[1]), dtype=np.float32)
        overlay_rgb = overlay

    # 배경 이미지에 오버레이 이미지 합성
    for c in range(0, 3):
        combined_background[:, :, c] = combined_background[:, :, c] * (1 - alpha_mask) + overlay_rgb[:, :, c] * alpha_mask

    # 랜덤 16진수 문자열 생성
    random_hex = ''.join(random.choice('0123456789ABCDEF') for _ in range(5))

    # 해당 디렉토리 내 파일 수 가져오기
    num_files = count_files(save_directory)

    # 파일 경로 생성
    file_path = f'{save_directory}/{num_files + 1}-{random_hex}.jpg'

    # 결과 이미지 저장
    cv2.imwrite(file_path, combined_background)

    # 원하는 출력 이미지 크기 지정 (예: 최대 가로 800, 최대 세로 900)
    max_width = 800
    max_height = 900

    # 원본 배경 이미지 크기
    original_height, original_width = combined_background.shape[:2]

    # 비율 유지하면서 크기 조정
    scaling_factor = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * scaling_factor)
    new_height = int(original_height * scaling_factor)

    # 크기 조정
    resized_background = cv2.resize(combined_background, (new_width, new_height))

    # 결과 출력
    cv2.imshow('Result', resized_background)

    # 마우스 이벤트 콜백 함수 등록
    cv2.setMouseCallback('Result', click_event)

    # 키 입력 대기
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 배경 이미지 리스트와 네 꼭짓점 좌표 (좌상, 우상, 우하, 좌하) 리스트
imgs = [
    ['C:/Users/lim16/Desktop/PhotoBox/sever/position_test/insert_imgs/insert.jpg',
     [[87, 640], [2500, 640], [1858, 2871], [99, 2859]]],
    ['C:/Users/lim16/Desktop/PhotoBox/sever/position_test/insert_imgs/insert.jpg',
     [[3039, 806], [5826, 815], [5826, 4282], [3029, 4292]]],
    ['C:/Users/lim16/Desktop/PhotoBox/sever/position_test/insert_imgs/insert.jpg',
     [[126, 4603], [2893, 4603], [2903, 8060], [135, 8069]]],
    ['C:/Users/lim16/Desktop/PhotoBox/sever/position_test/insert_imgs/insert.jpg',
     [[3029, 4418], [5807, 4437], [5816, 7895], [3039, 7904]]]
]

# 오버레이할 이미지 경로 (투명 PNG)
overlay_image_path = 'C:/Users/lim16/Desktop/PhotoBox/sever/position_test/test_img/2/1.png'

# 저장할 디렉토리
save_directory = 'C:/Users/lim16/Desktop/PhotoBox/sever/position_test/test_save'

# 함수 호출
overlay_images(imgs, overlay_image_path, save_directory)
