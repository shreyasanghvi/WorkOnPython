import cv2 as cv
import os as os
def ImgColorConversion(folder):
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            cv.imwrite(filename, gray)
        else:
            return "Something went wrong with image!"
    return "Images converted to gray scale and saved"