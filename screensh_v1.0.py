#Take Screenshots using Python and Save it in a file with a unique name
#pip install Pillow
from PIL import ImageGrab
import os

def yahscreensh():                                          #defines the function
    def check_img_in_current_folder(img):                   #checks if filename is in current directory
        return os.path.isfile(img) and os.path.exists(img)  
    file_name = "image"                                     #file name
    ext = ".png"                                            #file extension
    counter = 1                                             #incrementor
    img = file_name+ext                                     #stores image name 
    while check_img_in_current_folder(img):
        img = file_name+str(counter)+ext
        counter += 1                                        #increments the counter
    sc = ImageGrab.grab()                                   #takes the screenshot
    sc.save(img)                                            #saves the screenshot using the screenshot with a unique name 
    print(f"Image saved as {img}")                          #prints the output and our image result
yahscreensh()    