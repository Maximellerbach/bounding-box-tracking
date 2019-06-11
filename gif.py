import imageio
from glob import glob
from tqdm import tqdm
import cv2

size = (320,180)

filenames = glob('img\\*')#load images

with imageio.get_writer('img.gif', mode='I',duration=0.033) as writer:
    for filename in tqdm(filenames):
        image = imageio.imread(filename)
        image = cv2.resize(image,size)
        writer.append_data(image)