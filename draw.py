import os
import cv2
import numpy as np

def save_boxed_imgs(image_names, coord):
    input_images_names = os.listdir("FIR_images_v1/")

    for i in range(0,len(image_names)):

        if image_names[i] in input_images_names:

            image = cv2.imread(f"FIR_images_v1/{image_names[i]}")

            cv2.rectangle(image, coord[i], (0,255,0),1)
            cv2.imwrite(f"boxed_images/{image_names[i]}", image)

