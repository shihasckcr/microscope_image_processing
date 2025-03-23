import cv2

def select_roi(img_path, x, y, width, height, result_path):
    img = cv2.imread(img_path)
    roi = img[y:y + height, x:x + width]
    cv2.imwrite(result_path, roi)