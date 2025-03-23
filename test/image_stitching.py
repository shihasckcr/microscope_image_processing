import cv2
import numpy as np

def stitch_images(images):
    stitcher = cv2.Stitcher_create()
    status, stitched_image = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        print("Stitching completed successfully.")
        cv2.imshow("Stitched Image", stitched_image)
    else:
        print(f"Error during stitching: {status}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Sample Usage
image_paths = ['11.png', '12.png']
images = [cv2.imread(img_path) for img_path in image_paths if cv2.imread(img_path) is not None]

if len(images) >= 2:
    stitch_images(images)
else:
    print("Please provide at least two valid images for stitching.")
