# Click-n-Measure
## Overview
This uses OpenCV to measure the dimensions of objects in an image, detecting and measuring the height and width of object

## Features
- **Object Detection:** Identifies object within the image
- **Dimension Measurement:** Measures and displays the dimensions (height, width) of the detected objects
## Workflow
- OpenCV captures the image and preprocesses it by converting it to grayscale and applying thresholding to create a binary image
- The binary image is then processed to detect contours, which represent the boundaries of objects in the image
- Using these contours, the script calculates the dimensions of the bounding box around each detected object
- The measured dimensions are then annotated on the original image, displayed to the user

  ## Project Working
  ![](working2.png
)

