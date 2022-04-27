from shutil import move as mve
from time import sleep as slp
import os
import argparse
import shutil

def parse_args():
	desc = "Tool to crop an video" 
	parser = argparse.ArgumentParser(description=desc)

	parser.add_argument('--verbose', action='store_true',
		help='Print progress to console.')

	parser.add_argument('-i','--input_folder', type=str,
		default='./input/',
		help='Directory path to the inputs folder. (default: %(default)s)')

	parser.add_argument('-o','--output_folder', type=str,
		default='./output/',
		help='Directory path to the outputs folder. (default: %(default)s)')

	args = parser.parse_args()
	return args

source_path = "c:/Users/maxpg/Documents/AI/POSTER/UPSCALED/zusatz"
dest_path = "c:/Users/maxpg/Documents/AI/POSTER/UPSCALED/CROPPED"

def move_file(cropped_file):
    # get the current date
            # src_path = os.path.join(source_path, f)
            # create the folders if they arent already exists
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            # if not os.path.exists(f"{dest_path}\\{f}"):
            else:
                print("File already exists")
            mve(cropped_file, dest_path)

def crop_video(file_path):
    if file_path.endswith('.mp4'):
        print('cropping video: ' + file_path)
        
            

# while True:
files = os.listdir("c:/Users/maxpg/Documents/AI/POSTER/UPSCALED/zusatz")
for f in files:
    if f.endswith('.mp4'):
        print(f)
        pathname, extension = os.path.splitext(f)
        filename = pathname.split('/')
        print('{}_cropped.mp4'.format(filename[-1]))
        output_filename = "{}_cropped.mp4".format(filename[-1])
        os.system('ffmpeg -i zusatz/{} -filter_complex "crop=1450:in_h" -c:v libx264 -an {}'.format(f, output_filename))
        move_file(output_filename)
        print("END")
