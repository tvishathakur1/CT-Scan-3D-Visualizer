import dicomToNumpyCon
import numpyToObjCon
import fileSystem
import sys

print("System argument---")
print(sys.argv[0])

#calling the functions from here

#First converting dicom to numpy
numpyFromDicom = dicomToNumpyCon.main(fileSystem.dicomPath, "ctdata")

#now converting numpy to object
numpyToObjCon.main(numpyFromDicom, 250)

