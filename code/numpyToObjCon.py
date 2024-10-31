import numpy as np
import nibabel as nib
import pydicom as dicom
import pydicom.pixel_data_handlers.gdcm_handler
import os
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.ndimage
from skimage import morphology
from skimage import measure
from skimage.transform import resize
from sklearn.cluster import KMeans
import fileSystem

slash = fileSystem.slash
# cwd = os.getcwd() + slash + "ct_to3d" + slash
cwd = fileSystem.dir

imgPath = cwd + "skullct" + slash
outputPath = cwd + "output" + slash
numpyPath = cwd + "numpys" + slash

def marchingcubes_algo(numpy_from_dicom, threshold, step_size=1):
	print ("Transposing...")
	transpose = numpy_from_dicom.transpose(2,1,0)
	
	print ("Calculating marching cubes...")
	verts, faces, norm, val = measure.marching_cubes(transpose, threshold, step_size=step_size, allow_degenerate=True) 
	return verts, faces, norm

def makeObj(fPath, thisThreshold):
	if str(type(fPath)) == "<class 'numpy.ndarray'>":
		numpy_from_dicom = fPath
	else:
		try:
			numpy_from_dicom = np.load(numpyPath + fPath)
		except:
			print("Error while trying to load numpy loading, exiting...")
			exit()

	v, f, n = marchingcubes_algo(numpy_from_dicom, int(thisThreshold), 1)


	f=f+1

    
	newObj = open(outputPath + '%s.obj' % 'abd_output', 'w')
	print("Calculated marching cubes. Now making the obj file")
	for item in v:
		newObj.write("v {0} {1} {2}\n".format(item[0],item[1],item[2]))

	for item in n:
		newObj.write("vn {0} {1} {2}\n".format(item[0],item[1],item[2]))

	for item in f:
		newObj.write("f {0}//{0} {1}//{1} {2}//{2}\n".format(item[0],item[1],item[2]))  
	newObj.close()
	print("Successfully converted dicom array to object file!")

def main(mainFchoice, mainThreshold):
	print("Calling with two arguments--")
	makeObj(mainFchoice, mainThreshold)