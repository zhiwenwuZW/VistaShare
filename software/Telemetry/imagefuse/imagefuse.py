import os
import cv2
import numpy as np

def overlap_images(directory_path, alpha=0.5):
    # Get a list of image file names in the specified directory
    image_files = [f for f in os.listdir(directory_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

    # Check if there are at least two images in the directory
    if len(image_files) < 2:
        print("Insufficient images in the directory. Please provide at least two images.")
        return None

    # Read the first two images
    img1 = cv2.imread(os.path.join(directory_path, image_files[0]))
    img2 = cv2.imread(os.path.join(directory_path, image_files[1]))

    # Resize the images to the same dimensions (optional)
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Blend the images using alpha blending
    fused_image = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

    return fused_image

def crop_and_fill(directory_path, output_path, crop_region, scale_factor):
    # Get a list of image file names in the specified directory
    image_files = [f for f in os.listdir(directory_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

    # Check if there are at least two images in the directory
    if len(image_files) < 2:
        print("Insufficient images in the directory. Please provide at least two images.")
        return None

    # Read the first two images
    img1 = cv2.imread(os.path.join(directory_path, image_files[0]))
    img2 = cv2.imread(os.path.join(directory_path, image_files[1]))

    # Ensure that images are not None
    if img1 is None or img2 is None:
        print("Error: One or both images not found.")
        return

    # Check if the crop_array has four values (x, y, width, height)
    if len(crop_array) != 4:
        print("Error: The crop_array should have four values (x, y, width, height).")
        return

    # Extract values from the crop_array
    x, y, w, h = crop_array

    # Crop a region from the first image
    cropped_region = img1[y:y + h, x:x + w]

    # Scale a region from the second image
    scaled_region = cv2.resize(img2[y:y + h, x:x + w], (w, h))

    # Replace the cropped region in the first image with the scaled region from the second image
    img1[y:y + h, x:x + w] = cv2.addWeighted(cropped_region, 1 - scale_factor, scaled_region, scale_factor, 0)

    # Save the result
    cv2.imwrite(output_path, img1)

directory_path = "/Users/evan/PycharmProjects/VistaShare/image_test"
output_path = "/Users/evan/PycharmProjects/VistaShare/fuse_output/output_image.jpg"

crop_array = [1500, 1500, 500, 500]

# Specify the scale factor for the second image
scale_factor = 0.5

# Call the function
crop_and_fill(directory_path,output_path, crop_array, scale_factor)

# Display the result
result_image = cv2.imread(output_path)
cv2.imshow("Result", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
