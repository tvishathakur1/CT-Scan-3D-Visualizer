import os
import platform

slash = "\\"

# dir = os.getcwd() + slash + "ct_to3d" + slash
dir = os.getcwd() + slash
print("Current dire - ",dir)

dicomPath = dir + "ctdata" + slash
outputPath = dir + "output" + slash
numpyPath = dir + "numpys" + slash