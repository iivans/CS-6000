# -*- coding: utf-8 -*-
"""
@author: Isaac
"""

import os
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator
from PIL import Image

# Define the paths to the folders containing JPEG images
folder1_path = "normal"
folder2_path = "pneumonia"

# Function to display images from a folder in a grid
def display_images_in_grid(folder_path, num_columns=5):
    fig, axs = plt.subplots(1, num_columns, figsize=(15, 5))

    for i, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            try:
                # Open and display the image in grayscale in the current subplot
                img = Image.open(image_path).convert('L')
                axs[i % num_columns].imshow(img, cmap='gray')
                axs[i % num_columns].set_title(filename)
                axs[i % num_columns].axis('off')
            except Exception as e:
                print(f"An error occurred while opening {image_path}: {str(e)}")

    # Remove empty subplots
    for i in range(len(os.listdir(folder_path)), num_columns):
        fig.delaxes(axs[i])

    plt.show()

# Display images from folder1 in a grid
print(f"Displaying images from {folder1_path} in a grid:")
display_images_in_grid(folder1_path)

# Display images from folder2 in a grid
print(f"Displaying images from {folder2_path} in a grid:")
display_images_in_grid(folder2_path)