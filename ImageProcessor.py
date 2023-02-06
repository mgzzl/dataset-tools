import argparse
import os
from PIL import Image
import threading

class ImageProcessor:
    def __init__(self, input_dir:str, dimension:str, size:int, output_dir:str):
        self.input_dir = input_dir
        self.dimension = dimension
        self.size = size
        self.output_dir = output_dir

    def get_images(self, input_dir):
        images = []
        # Use the os.listdir() method to list the files in the directory
        for file in os.listdir(input_dir):
            # Use the os.path.join() method to create the full path to the file
            file_path = os.path.join(input_dir, file)

            # Use the os.path.isfile() method to check if the file is a regular file (not a directory)
            if os.path.isfile(file_path) and (file_path.endswith('.jpg') or file_path.endswith('.png')):
                images.append(file_path)

        return images

    def resize_img(self, img, resize_size, dimension):
        if dimension == "height":
            # Calculate the width of the resized image using the desired height and the aspect ratio of the original image
            width = int(img.width * resize_size / img.height)

            # Resize the image using the calculated width and the desired height
            resized_img = img.resize((width, resize_size))
        else:
            # Calculate the height of the resized image using the desired width and the aspect ratio of the original image
            height = int(img.height * resize_size / img.width)

            # Resize the image using the desired width and the calculated height
            resized_img = img.resize((resize_size, height))

        # return the resized image
        return resized_img

    def crop_img(self, img, crop_size, dimension):
        if dimension == "height":
            # Calculate the left and right crop coordinates using the crop_width value and the image dimensions
            left = int((img.width - crop_size) / 2)
            right = left + crop_size

            # Crop the image using the calculated coordinates
            cropped_img = img.crop((left, 0, right, img.height))
        else:
            # Calculate the top and bottom crop coordinates using the crop_height value and the image dimensions
            top = int((img.height - crop_size) / 2)
            bottom = top + crop_size

            # Crop the image using the calculated coordinates
            cropped_img = img.crop((0, top, img.width, bottom))
        return cropped_img

    def process_img(self, image_path:str):
        # Open the image using the file_path variable
        with Image.open(image_path) as img:
            resized_img = self.resize_img(img,self.size,self.dimension)
            cropped_img = self.crop_img(resized_img, self.size, self.dimension)
            root, extension = os.path.splitext(image_path)
            filename = os.path.basename(root)
            # if not os.path.exists(self.output_dir):
            #   os.mkdir(self.output_dir)
            cropped_img.save(f'{self.output_dir}/{filename}-processed{extension}')
            # cropped_img.save(f'{self.output_dir}/{filename}-processed.jpg')

    def process_imgs(self):
        images = self.get_images(self.input_dir)

        # Create a list of threads
        threads = []

        # Loop over the list of images and create a new thread for each image
        for image_path in images:
            thread = threading.Thread(target=self.process_img, args=(image_path,))
            threads.append(thread)

        # Start the threads
        for thread in threads:
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", type=str, required=True, help="Input directory path")
  parser.add_argument("-d", "--dimension", type=str, required=True, help="Dimension (height/width) to resize and crop the images")
  parser.add_argument("-s", "--size", type=int, required=True, help="Size to resize and crop the images")
  parser.add_argument("-o", "--output", type=str, required=True, help="Output directory path to save the processed images")
  args = parser.parse_args()

  processor = ImageProcessor(args.input, args.dimension, args.size, args.output)
  processor.process_imgs()