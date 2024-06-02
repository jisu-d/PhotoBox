import json
import cv2
import random
import os
import base64
from io import BytesIO
from PIL import Image
import numpy as np

def count_files(directory):
    files = os.listdir(directory)
    file_count = len(files)
    return file_count

def add_overlays(foreground, backgrounds):
    foreground_height, foreground_width, _ = foreground.shape

    # 검정색 배경 이미지 생성
    black_background = np.zeros((foreground_height, foreground_width, 3), dtype=np.uint8)

    for image_data, points in backgrounds:
        overlay_data = base64.b64decode(image_data)
        overlay_image = Image.open(BytesIO(overlay_data))
        overlay_np = cv2.cvtColor(np.array(overlay_image), cv2.COLOR_RGB2BGR)
            
        h, w = overlay_np.shape[:2]
            
        # 네 꼭짓점 좌표 계산
        src_points = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)
        dst_points = np.array(points, dtype=np.float32)
            
        # 투영 변환 매트릭스 계산
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)
            
        # 이미지 변환
        warped_overlay = cv2.warpPerspective(overlay_np, matrix, (black_background.shape[1], black_background.shape[0]))
            
        # 마스크 생성
        mask = np.zeros_like(black_background, dtype=np.uint8)
        cv2.fillConvexPoly(mask, np.int32([dst_points]), (255, 255, 255))
        mask_inv = cv2.bitwise_not(mask)
            
        # 배경 이미지와 합성
        black_background = cv2.bitwise_and(black_background, mask_inv)
        black_background = cv2.bitwise_or(black_background, warped_overlay)

    # 알파 채널 분리
    foreground_alpha = foreground[:, :, 3]
    foreground_rgb = foreground[:, :, :3]

    # 알파 채널을 3채널로 확장
    foreground_alpha_expanded = np.expand_dims(foreground_alpha, axis=2)
    foreground_alpha_expanded = np.repeat(foreground_alpha_expanded, 3, axis=2)

    # 배경 이미지와 전경 이미지 합치기
    result = cv2.multiply(black_background.astype(float), (1 - (foreground_alpha_expanded / 255)))
    result += cv2.multiply(foreground_rgb.astype(float), (foreground_alpha_expanded / 255))
    result = result.astype(np.uint8)

    return result

def save_image_with_count_and_random_hex(background, directory):
    random_hex = ''.join(random.choice('0123456789ABCDEF') for _ in range(5))
    num_files = count_files(directory)
    file_path = f'{directory}/{num_files + 1}-{random_hex}.jpg'
    cv2.imwrite(file_path, background)
    return file_path

def resize_image(background, max_width, max_height):
    original_height, original_width = background.shape[:2]
    scaling_factor = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * scaling_factor)
    new_height = int(original_height * scaling_factor)
    resized_background = cv2.resize(background, (new_width, new_height))
    return resized_background

def read_json():
    # JSON 파일 경로
    file_path = "C:/Users/lim16/Desktop/PhotoBox/sever/frame_info.json"
    # file_path = "/home/jisu/project/PhotoBox/sever/frame_info.json"

    # JSON 파일 열기
    with open(file_path, "r") as json_file:
        # JSON 데이터 로드
        data = json.load(json_file)

    return data

def find_data_by_title(title, data):
    for item in data:
        if item["title"] == title:
            return item
    return None

def creative_collage_images(data):
    frameData = read_json()
    # 특정 title에 대한 데이터 찾기
    result = find_data_by_title(data.title, frameData)

    overlays = []
    for points, img_select in zip(result['imgs_info'], data.select_imgs):
        base64_data = img_select  # 이미지 데이터
        overlay = (base64_data, points)
        overlays.append(overlay)

    title_parts = data.title.split('-')

    background = cv2.imread(f'C:/Users/lim16/Desktop/PhotoBox/sever/frame/{title_parts[0]}/{title_parts[1]}.png', cv2.IMREAD_UNCHANGED)
    # background = cv2.imread(f'/home/jisu/project/PhotoBox/sever/frame/{title_parts[0]}/{title_parts[1]}.png', cv2.IMREAD_UNCHANGED)

    background_with_overlays = add_overlays(background, overlays)

    resized_background = resize_image(background_with_overlays, 800, 900)

    file_path = save_image_with_count_and_random_hex(background_with_overlays, 'C:/Users/lim16/Desktop/PhotoBox/sever/save')
    # file_path = save_image_with_count_and_random_hex(background_with_overlays, '/home/jisu/project/PhotoBox/sever/save')

    # OpenCV를 통해 이미지를 Bytes 형태로 변환
    _, encoded_image = cv2.imencode('.jpg', resized_background)

    # cv2.imshow('Result', resized_background)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Bytes 데이터를 base64로 인코딩
    base64_encoded_image = base64.b64encode(encoded_image).decode('utf-8')

    # base64로 인코딩된 이미지 데이터 반환
    return file_path, base64_encoded_image