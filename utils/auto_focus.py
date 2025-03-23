import cv2
import numpy as np

def auto_focus(img_path, result_path):
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap_var = cv2.Laplacian(gray_img, cv2.CV_64F).var()

    if lap_var < 100:
        sharpened = cv2.filter2D(img, -1, np.array([[-1, -1, -1],
                                                      [-1,  9, -1],
                                                      [-1, -1, -1]]))
        cv2.imwrite(result_path, sharpened)
    else:
        cv2.imwrite(result_path, img)
