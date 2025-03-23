import cv2
import numpy as np

def stitch_images(image_paths, result_path):
    images = [cv2.imread(img) for img in image_paths]
    stitcher = cv2.Stitcher_create()
    status, stitched_image = stitcher.stitch(images)
    if status == cv2.Stitcher_OK:
        cv2.imwrite(result_path, stitched_image)
        print("Stitching completed successfully.")
    else:
        print(f"Error during stitching: {status}")