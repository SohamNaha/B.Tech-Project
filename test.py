import os
import numpy as np
import nibabel as nib
from  matplotlib import pyplot as plt
from PIL import Image

# interactively ask for the .nii file
from tkinter.filedialog import askopenfilename
filename = askopenfilename()

#from nibabel.testing import data_path
image = nib.load(filename)
print(image.shape[:-1])			#image size in pixels
print(image.get_data_dtype())	#image data type

# The get_data() function returns a standard NumPy multi-dimensional array, so you can treat it as you would any other ndarray.
image_data = image.get_data()
img = Image.fromarray(image_data)
img