
import pip 

def install(package) :
     pip.main(['install', package])
     

try:
     from rembg import remove
     from tkinter import *
     from tkinter import filedialog
except:
    install("rembg")
    install("-U Pillow")  
    install("tkinter") 


from PIL import Image
from rembg import remove
from tkinter import *
from tkinter import filedialog

def openfile():
    filepath=filedialog.askopenfilename()
    global value
    value = filepath
    
window = Tk()
window.title('image background remover')
# Set window size
window.geometry("400x100")
#Set window background color
window.config(background = "black")
button= Button(text="select the image location",command=openfile)
button.pack()
window.mainloop()

input_path = value

output_path = 'output.png'

input = Image.open(input_path)

output = remove(input)

output.save(output_path)





