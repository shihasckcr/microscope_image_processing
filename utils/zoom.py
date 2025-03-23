import cv2
import numpy as np

def zoom_image(image_path, zoom_factor, result_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    height, width = image.shape[:2]

    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

    zoomed_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite(result_path, zoomed_image)
    cv2.imshow(f"Zoomed Image ({zoom_factor}X)", zoomed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    print(f"Zoom applied successfully with factor {zoom_factor}")