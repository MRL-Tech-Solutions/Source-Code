import cv2

# Define the path to the image
image_path = r'C:/Users/ADMIN/AppData/Local/Programs/Python/Python310/face/Pencil Sketch/anushka-shetty.jpg'

# Read the image
image = cv2.imread(image_path)
if image is None:
    print("Error loading image")
else:
    # Display the original image
    cv2.imshow("Rabbit", image)
    cv2.waitKey(0)

    # Convert to gray scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", gray_image)
    cv2.waitKey(0)

    # Invert the image
    inverted_image = 255 - gray_image
    cv2.imshow("Inverted", inverted_image)
    cv2.waitKey(0)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # Display the pencil sketch
    cv2.imshow("Pencil Sketch", pencil_sketch)
    cv2.waitKey(0)

    # Optionally, display both original and sketch in one window
    cv2.imshow("Original + Sketch", cv2.hconcat([image, pencil_sketch]))
    cv2.waitKey(0)

# Clean up windows
cv2.destroyAllWindows()
