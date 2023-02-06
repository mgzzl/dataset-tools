import glob
from PIL import Image

# Set the desired height and width of the images
desired_height = 512
desired_width = 512

# Find all the images in the given directory
images = glob.glob("./img/*.png")

# Iterate over the images
for image_path in images:
    # Open the image
    img = Image.open(image_path)
    # Calculate the width of the resulting image
    aspect_width = round(img.width / img.height * desired_height)

    # Scale the height of the image
    img = img.resize((aspect_width, desired_height))

    # Calculate the width to be cropped from the center
    width_to_crop = (img.width - desired_width) / 2

    # Crop the width of the image
    img = img.crop((width_to_crop, 0, img.width - width_to_crop, img.height))

    # Save the resulting image
    img.save("./img-processed/cropped.png")
