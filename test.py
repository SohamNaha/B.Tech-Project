import os
import numpy as np
import nibabel as nib
from  matplotlib import pyplot as plt
from PIL import Image

# interactively ask for the .nii file
from tkinter.filedialog import askopenfilename
filename = askopenfilename(title="Open File")

# to get folder directory
c = '/'
index = [pos for pos, char in enumerate(filename) if char == c]
last = index[-1]
directory = filename[:last]
print(directory)

#from nibabel.testing import data_path
image = nib.load(filename)
a = image.shape
print(a)		      	#image size in pixels
print(image.get_data_dtype())	#image data type

# The get_data() function returns a standard NumPy multi-dimensional array, so you can treat it as you would any other ndarray.
image_data = image.get_data()

for i in range(a[-1]):
	fig = plt.figure()
	fname = 'image'+str(i)+'.png'
	full_path = directory + '/' + fname
	plt.savefig(full_path , dpi=fig.dpi , bbox_inches='tight')
	plt.imshow(image_data[:,:,i])
