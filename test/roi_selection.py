import cv2
import numpy as np

def select_roi(image_path, x, y, width, height):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    roi = image[y:y+height, x:x+width]

    cv2.imshow("Selected ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Sample Usage
image_path = '12.png'  # Replace with your image path
x, y, width, height = 100, 150, 200, 200  # Example coordinates
select_roi(image_path, x, y, width, height)