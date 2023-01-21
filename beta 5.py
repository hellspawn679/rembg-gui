import pip
import os
# install given module from pip
def install(package):
    pip.main(['install', package])
# test if the module is there if not then it will install it
try:
    from rembg import remove
    from tkinter import *
    from tkinter import filedialog
except:
    install("rembg")
    install("-U Pillow")
    install("tkinter")
# it will open the file explores and will give you the location of the chosen file
def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users",title="choose the image file ",filetypes= [("image file" ,".png .jpeg .jpg"),("all files","*.*")])
    global value
    value = filepath
    global u
    u = 1
    outfolder()
#it will open the file explores and will ask you for folder location
def openfolder():
    folderpath = filedialog.askdirectory(initialdir="C:\\Users",title="choose the input folder ")
    global value
    value = folderpath
    global u
    u = 0
    outfolder()
#it will ask for output folder for one folder file
def outfolder():
    outpath = filedialog.askdirectory(initialdir="C:\\Users",title="choose the output folder ")
    global value2
    value2 =outpath
    window.destroy()
#it will ask for output folder for one image file 
def outimage():
    outpath=filedialog.askdirectory(initialdir="C:\\Users",title="choose the output folder ")
    global value2
    value2 =outpath
    window.destroy()
# FOR one image function
def oneimg(value):
    input_path = value
    # will store the image
    print(value2)
    output_path = value2+"/output.png"
    input = IMG.open(input_path)
    # will remove the background ig
    output = remove(input)
    output.save(output_path)
#for one folder function 
def onefolder(value):
    cmd = "rembg p " + value +" "+ value2

    os.system(cmd)
from tkinter import filedialog
from tkinter import *
from rembg import remove
from PIL import Image as IMG

window = Tk()
window.title('image background remover')
# Set window size
window.geometry("400x100")
# Set window background color
window.config(background="black")
# it descripbe what the button do and what should be written on the buttom
button = Button(text="select the image location", command=openfile)
button2 = Button(text="select a input /output folder location", command=openfolder)
#this is for spaces in the label 
label=Label(window,text="                                             ")
label.grid(row=0,column=0)
label.grid(row=1,column=0)
button.grid(row=0, column=1)
button2.grid(row=1, column=1)

# will run the window showing process
window.mainloop()

if u == 1:
    oneimg(value)
else:
    onefolder(value)
