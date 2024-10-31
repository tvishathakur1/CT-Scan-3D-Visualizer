# 3D Visualization of CT Scan Images

## Contents
1. [Introduction](#introduction)  
2. [About Project](#about-project)  
3. [What Was Achieved](#what-was-achieved)  
4. [Challenges Faced](#challenges-faced)  
5. [Conclusion](#conclusion)  

## Introduction
Medical imaging has revolutionized the way various diseases are diagnosed and treated. With advancements in tools like the CT scan (Computed Tomography) and the MRI scan (Magnetic Resonance Imaging), medical professionals find it easy to identify and characterize abnormalities in the human body. A CT scan produces multiple 2D cross-sectional images of an organ or a body part. Interpreting these images can be challenging, and visualizing the complex structures and relationships within the data can be even more so.

![image](https://github.com/user-attachments/assets/5e075ff0-06b9-4c02-9da4-b99ed5c91f25)

## About Project
This project is about converting CT scan data to a 3D object. The goal of this project is to make it easier for doctors and other medical professionals to visualize and understand the structures they're looking at.

### Technologies Used:
- **Python**: The primary programming language used to read, visualize, and convert the data into a 3D model. Python is versatile and has various libraries that helped in the accomplishment of this project.
  
#### Key Libraries:
- **Pydicom**: A Python package used to work with DICOM data, allowing for reading, modifying, and manipulating DICOM data.
- **SciPy**: Used for scientific computing, including linear algebra, integration, and interpolation. In this project, it is used for the interpolation and resampling of data.
- **Scikit-image**: A Python package for image processing. The marching cubes algorithm from this package is used in the project.

### Project Steps:
1. **Data Collection**: Collecting CT scan data from medical institutions or open-source websites that provide sample CT scan data in DICOM format.
2. **Reading DICOM Data**: Utilizing Python libraries to read and process the DICOM data.
3. **Converting to Numpy Array**: The DICOM data is converted into a numpy array representing Hounsfield units (a scale that describes radiodensity and is used to represent CT scans).
4. **Converting to .obj File**: The numpy array of pixels is converted to a 3D object file using the marching cubes algorithm.

## What Was Achieved
This project has successfully converted multiple 2D DICOM images to a 3D object using various Python libraries. The 3D object provides a better understanding of the CT scan and the underlying details, aiding medical professionals in analyzing and diagnosing conditions easily and accurately.

### Input CT Scans:
1. Abdomen CT scan
2. Arm CT scan

#### Results:
- **Abdomen 3D Object**  
  ![image](https://github.com/user-attachments/assets/26f5a570-0a8d-44e2-b3d7-2f2aaffcba47)
  ![image](https://github.com/user-attachments/assets/a198debe-2cca-4a99-979d-398c890121a4)

- **Arm 3D Object**  
  ![image](https://github.com/user-attachments/assets/f05a25b0-9334-4ed7-9d6a-df105112dde0)
  ![image](https://github.com/user-attachments/assets/0ff799a4-1b77-4db6-b9eb-357c30ea18d5)

### Reasons:
- The quality of the CT scan data may have included noise, affecting the reconstructed 3D object.
- Limitations of the techniques and algorithms used; there is always room for improvement.

## Challenges Faced
1. **Collection of CT Data**: The primary challenge was obtaining CT scan data, as sample CT scan DICOM data are often subject to privacy regulations and are confidential.
2. **Format of the Data**: The CT data must be in a specific DICOM format, and not all DICOM files have the required attributes, making it challenging to find compatible files.

## Conclusion
Despite the challenges and limitations encountered, this project was engaging and rewarding. Successfully converting CT scans to 3D objects demonstrated the versatility of Python as a programming language, which offers numerous packages to analyze and work with different types of data.
