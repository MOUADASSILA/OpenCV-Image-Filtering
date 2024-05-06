#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:26:06 2024

@author: mac
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:37:47 2024

@author: mac
"""
import cv2
import matplotlib.pyplot as plt  # Import pyplot for displaying images

image_path = "/Users/mac/Downloads/original.png"
image = cv2.imread(image_path)  # Read the image from the given path

if image is None:
    print("Image not found. Please check the path.")
else:
    kernel_size = (6, 6)
    main_filtered_image = cv2.blur(image, kernel_size)

    # Convert the image from BGR to RGB
    main_filtered_image_rgb = cv2.cvtColor(main_filtered_image, cv2.COLOR_BGR2RGB)

    # Display the image using matplotlib
    plt.imshow(main_filtered_image_rgb)
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

    # Save the filtered image
    cv2_filtered_image_path = "cv2_mean_filtered_image.png"
    cv2.imwrite(cv2_filtered_image_path, main_filtered_image)
