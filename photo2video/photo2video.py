import cv2
import numpy as np
import os

outputdir = 'ouput.mp4'
inputdir = 'photos/'
fps = 15

if __name__ == '__main__':
    fo = open('namelist.txt')
    name = fo.readline()
    img = cv2.imread(inputdir+name[0:len(name)-1])
    imgsize = img.shape
    print imgsize
    fo.close()
    fo = open('namelist.txt')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    videoWriter = cv2.VideoWriter(outputdir,fourcc,fps,(imgsize[1],imgsize[0]))
    for name in fo:
        name = name[0:len(name)-1]
        img = cv2.imread(inputdir+name,3)
        videoWriter.write(img)
        print name
        print img.shape
    videoWriter.release()
    print 'everything done'
