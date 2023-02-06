from PIL import Image
import os
import shutil

class ImageSorter:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    def sort_images(self):
        for filename in os.listdir(self.input_directory):
            filepath = os.path.join(self.input_directory, filename)
            if os.path.isfile(filepath):
                self.move_image(filepath)

    def move_image(self, filepath):
        with Image.open(filepath) as img:
            width, height = img.size

        if width > height:
            dirname = 'landscape'
        elif width < height:
            dirname = 'portrait'
        else:
            dirname = 'square'

        dirpath = os.path.join(self.output_directory, dirname)
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)

        shutil.move(filepath, dirpath)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_directory", required=True, help='Directory containing the images to sort')
    parser.add_argument("-o", "--output_directory", default=None, help='Directory where the sorted images should be saved. Directory will be created if not exist. default: input_directory')
    args = parser.parse_args()

    # Set the default output directory to the input directory if not specified
    if args.output_directory is None:
        args.output_directory = args.input_directory

    image_sorter = ImageSorter(args.input_directory, args.output_directory)
    image_sorter.sort_images()
