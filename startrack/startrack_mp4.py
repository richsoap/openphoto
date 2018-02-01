import cv2
import os
import numpy as np

inputdir = 'videos/'
fadefactor = 0

outputdir = 'ouput_' + str(fadefactor) + '.mp4'
fps = 25

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
    maxValue = 0
    fo = open('namelist.txt')
    name = fo.readline()
    img = cv2.imread(inputdir+name[0:len(name)-1])
    imgsize = img.shape
    outputsize = tuple([imgsize[1],imgsize[0]])
    print imgsize
    fo.close()
    fo = open('namelist.txt')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    videoWriter = cv2.VideoWriter(outputdir,fourcc,fps,(imgsize[1],imgsize[0]))
    cimg = np.zeros([imgsize[0],imgsize[1],imgsize[2]])
    for name in fo:
        name = name[0:len(name)-1]
        print name
        img = cv2.imread(inputdir+name,3)
        img = cv2.resize(img,outputsize,cv2.INTER_AREA)
        cimg = np.multiply(cimg,fadefactor)
        cimg = np.uint16(np.around(cimg))
        cimg = merage(cimg,img)
        cimg = np.uint16(np.around(cimg))
        cv2.imwrite('temp.jpg',cimg)
        print 'cimg size:' + str(cimg.shape)
        cimg = cv2.imread('temp.jpg')
        videoWriter.write(cimg)
    videoWriter.release()
