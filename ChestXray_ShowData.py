# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:37:52 2023

@author: Isaac

Create a public GitHub repository and share the link to that repository here.

Your repository should include:

3 datasets you provided in the Selecting a Thesis Topic discussion.
3 Python programs that import and display each individual dataset.
Consider using Google Colab or Jupyter Notebooks, and the NumPy, pandas, and Matplotlib libraries.
3 images, one for each Python program output.
1 PDF file ranking the datasets based on feasibility, access, display, and understanding.
"""

import pandas as pd

# Define the file path
file_path = "BBox_List_2017_Chest_XRay.csv"

try:
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Display the entire DataFrame
    print(df)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
