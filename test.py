#importing modules
import os
import numpy as np
import nibabel as nib
from  matplotlib import pyplot as plt
from PIL import Image
from nilearn import plotting
from pyunpack import Archive
from tkinter.filedialog import askopenfilename

# interactively ask for the .nii.gz file
filename = askopenfilename(title="Open File")
print(filename)

# to get folder directory
c = '/'
index = [pos for pos, char in enumerate(filename) if char == c]
last = index[-1]
directory = filename[:last]
print(directory)

Archive(filename).extractall(directory)    #extracting .nii file

os.mkdir(filename+' images')     #creating folder to store images

image = nib.load(filename)       #from nibabel.testing import data_path
print(image.shape)
n = image.shape			#image size in pixels
m = n[-1]
print(image.get_data_dtype())	#image data type
image_data = image.get_data()


#image sets
for i in range(m):
	plt.imshow(image_data[:,:,i], cmap='hot')
	fig=plt.gcf()
	fig.savefig(filename+' images' +'/'+ 'image' + str(i) + '.png' , bbox_inches='tight')

# interactively ask for the  extracted .nii file
filename1 = askopenfilename(title="Open File")

image1 = nib.load(filename1)

fig1=plotting.plot_stat_map(image1)
fig1.savefig(filename+' images' +'/'+ 'statiscal map' + '.png')
fig2=plotting.plot_glass_brain(image1)
fig2.savefig(filename+' images' +'/'+ 'glass plot' + '.png')

