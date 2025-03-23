import cv2
import numpy as np

def auto_focus(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()

    if laplacian_var < 100:  # Low sharpness threshold (adjustable)
        sharpened = cv2.filter2D(image, -1, np.array([[0, -1, 0],
                                                      [-1, 5, -1],
                                                      [0,-1, 0]]))
        print("Image sharpened to improve focus.")
        cv2.imshow("Auto-Focus Result", sharpened)
    else:
        print("Image clarity is sufficient.")
        cv2.imshow("Auto-Focus Result", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'Untitled design.png'  
auto_focus(image_path)
