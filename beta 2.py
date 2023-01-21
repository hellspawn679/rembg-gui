import os
cmd3 = "pip install pyautogui"
os.system(cmd3)
cmd = "pip install rembg"
cmd2 = "pip install -U Pillow"
os.system(cmd)
os.system(cmd2)
from rembg import remove
from PIL import Image
import pyautogui
value = pyautogui.prompt("enter the path of image in the dir ")
input_path = str(value)
print(value)
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)