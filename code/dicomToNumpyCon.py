import numpy as np
import pydicom as dicom
import os
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import scipy.ndimage
import fileSystem
import time

def process_input_scan(scanPath=fileSystem.dicomPath + fileSystem.slash):
	dicom_array = [dicom.read_file(scanPath + fileSystem.slash + s) for s in os.listdir(scanPath)]
	# print("Type of dicom_array is-- ", type(dicom_array[0])) #pydicom.dataset.FileDataset
	dicom_array.sort(key = lambda x: int(x.InstanceNumber))
	try:
		slice_thickness = np.abs(dicom_array[0].ImagePositionscan[2] - dicom_array[1].ImagePositionscan[2])
	except:
		slice_thickness = np.abs(dicom_array[0].SliceLocation - dicom_array[1].SliceLocation)
		
	for s in dicom_array:
		s.SliceThickness = slice_thickness
		
	return dicom_array

def dicom_to_hu(dicom_array):
	image = np.stack([s.pixel_array for s in dicom_array])
	# print("pixel array print-- ",dicom_array[0].pixel_array)
	image = image.astype(np.int16)

	image[image == -2000] = 0
	
	# Converting to Hounsfield units (HU)
	intercept = dicom_array[0].RescaleIntercept
	slope = dicom_array[0].RescaleSlope
	
	if slope != 1:
		image = slope * image.astype(np.float64)
		image = image.astype(np.int16)
		
	image += np.int16(intercept)
	
	return np.array(image, dtype=np.int16)

def dataResampling(dataPath=fileSystem.dicomPath, new_spacing=[1,1,1]):
	scannedData = process_input_scan(dataPath)
	image = dicom_to_hu(scannedData)

	print ("Before resampling, shape of hu data\t", image.shape)

	start = time.perf_counter()
	# Determine current pixel spacing
	try:
		spacing = map(float, ([scannedData[0].SliceThickness] + [scannedData[0].PixelSpacing[0], scannedData[0].PixelSpacing[1]]))
		spacing = np.array(list(spacing))
	except:
		print(len(scannedData[0].PixelSpacing))
		print ("Pixel Spacing (row, col): (%f, %f) " % (scannedData[0].PixelSpacing[0], scannedData[0].PixelSpacing[1]))
		print("exiting?")
		exit()

	resize_factor = spacing / new_spacing
	new_real_shape = image.shape * resize_factor
	new_shape = np.round(new_real_shape)
	real_resize_factor = new_shape / image.shape
	new_spacing = spacing / real_resize_factor
	
	image = scipy.ndimage.interpolation.zoom(image, real_resize_factor)
	print ("dataResampling done in:  " + str(time.perf_counter()-start))
	print ("After resample, shape obtained \t", image.shape)
	
	return image, new_spacing

def main(inputPath=fileSystem.dicomPath, mainFname="ctdata"):
	resamp_output, spacing = dataResampling(inputPath)
	# if option == 1:
	# 	np.save(fileSystem.numpyPath + "%s.npy" % mainFname, resamp_output)
	# 	return 0
	return resamp_output