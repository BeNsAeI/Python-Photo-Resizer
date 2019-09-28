import pip
from os import walk

if int(pip.__version__.split('.')[0])>9:
        from pip._internal import main
else:
        from pip import main
main(['install', "numpy"])
main(['install', "opencv-python"])

import numpy as np
import cv2

class Resize:
    def __init__(self,in_path,out_path):
        self.in_path = in_path
        self.out_path = out_path
        return

    def rename_batch(self,in_path,out_path):
        files = []
        for (dirpath, dirnames, filenames) in walk(in_path):
                files.extend(filenames)
                break
        print("Total size: ", len(files))
        
        from shutil import copyfile
        i = 0;
        for file in files:
                extention = file.split(".")[1]
                if (extention == "jpg") or (extention == "jpeg"):
                        i += 1
                        copyfile(in_path +'\\'+file, out_path+'\\'+str(i)+".jpg")
                        print(str(i) + ": " + file + " was copied.")
                else:
                        print(file + " was ommited.")
        return

    def resize(self,multiplier):
        files = []
        for (dirpath, dirnames, filenames) in walk(self.in_path):
                files.extend(filenames)
                break
        print("Number of images:", len(files))
        for file in files:
                path = self.in_path+"\\"+file
                new_path = self.out_path+"\\"+file
                print("Processing:",path)
                img = cv2.imread(path,1)
                height, width, depth = img.shape
                dim = (round(width*multiplier), round(height*multiplier))
                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                print("New dimentions are: "+ str(height) + "x" + str(width)+".")
                cv2.imwrite(new_path,resized)
                print("Saved to",new_path)
        return

    def resize_large(self):
        self.resize(0.75)
        return

    def resize_medium(self):
        self.resize(0.5)
        return

    def resize_small(self):
        self.resize(0.25)
        return

def main():
    # Initiate the opbejcts
    my_large_resize = Resize("..\Raw_renamed","..\Resized\Large")
    my_medium_resize = Resize("..\Raw_renamed","..\Resized\Medium")
    my_small_resize = Resize("..\Raw_renamed","..\Resized\Small")
    
    # Rename the images for ease of handling if needed
    #my_large_resize.rename_batch("..\Raw","..\Raw_renamed")
    
    # Call in the resize functions:
    my_large_resize.resize_large()
    my_medium_resize.resize_medium()
    my_small_resize.resize_small()
  
if __name__== "__main__":
    main()
