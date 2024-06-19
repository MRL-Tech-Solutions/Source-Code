import cv2
import os

# Load the Haar cascade files for face and eye detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Define the path to the images directory
images_path = r'C:\Users\ADMIN\AppData\Local\Programs\Python\Python310\face\Image detection - done\dataset'

# Get the list of image filenames
image_filenames = [f for f in os.listdir(images_path) if f.endswith('.jpg')]

# Sort the filenames in ascending order
image_filenames.sort()

# Loop through each image filename
for filename in image_filenames:
    # Load the image
    image = cv2.imread(os.path.join(images_path, filename))

    # Resize the image
    image = cv2.resize(image, (0, 0), fx=0.2, fy=0.2)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(10, 10))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Detect eyes in the image
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1, minSize=(10,10))

    # Draw rectangles around the eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)

    # Display the output image
    cv2.imshow('Output', image)

    # Wait for 200 milliseconds (0.2 seconds) or until the window is closed
    cv2.waitKey(1000)

# Destroy all windows
cv2.destroyAllWindows()
