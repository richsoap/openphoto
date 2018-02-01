import cv2
import os
import numpy as np

inputdir = 'photos/'
fadefactor = 0.99
tensfactor = 2.5

def merage(img1,img2):
    gimg1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    print gimg1.shape
    gimg2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    index1 = gimg1 < gimg2
    index2 = gimg1 >= gimg2
    resultimg = np.zeros(img1.shape)
    resultimg[index1] = img2[index1]
    resultimg[index2] = img1[index2]
    return resultimg


if __name__ == '__main__':
    fo = open('namelist.txt')
    cimg = []
    maxValue = 0
    count = 0
    for name in fo:
        count = count + 1
        name = name[0:len(name)-1]
        print name
        img = cv2.imread(inputdir+name,cv2.IMREAD_COLOR)
        test = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        print img.shape
        maxValue = max(np.max(img),maxValue)
        if cimg == []:
            cimg = img
            continue
        tempimg = np.uint16(np.around(np.multiply(cimg,fadefactor)))
        cimg = merage(tempimg,img)
    tempMax = np.max(cimg)
    cimg = np.divide(cimg,tempMax)
    cimg = cimg**tensfactor
    cimg = np.multiply(maxValue,cimg)
    cimg = np.uint16(np.around(cimg))
    cv2.imwrite('output' + str(fadefactor) + '.jpg',cimg)
