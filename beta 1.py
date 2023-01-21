from rembg import remove
from PIL import Image

input_path = '90.jpg' # input image path
output_path = 'output.png' # output image path

input = Image.open(input_path) # load image
output = remove(input) # remove background
output.save(output_path) # save image