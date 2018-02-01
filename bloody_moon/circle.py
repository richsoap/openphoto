import cv2
import numpy as np
import os

photodir = "photos/"
outputdir = "output/"
tempdir = "temp/"
photosize = [6000,4000]
clipsize = [1280,720]
outputsize = [1920,1080]

def min(a,b):
	if a < b:
		return a
	else:
		return b

def getCenter(photoname):
	img = cv2.imread(photodir+photoname,0)
	photosize = img.shape
	img = cv2.medianBlur(img,5)
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist=500,param1=50,param2=50,minRadius=0,maxRadius=0)#find where the moon is,param1 means fading param in canny filter, param2 means round rate
	print photoname
	circles = np.uint16(np.around(circles))
	circles = circles[0][0]#one picture one moon
	cimg = cv2.circle(cimg,(circles[0],circles[1]),circles[2],(0,255,255),4)
	cv2.imwrite(tempdir + photoname,cimg)
	cutImg(photoname,circles)
	print circles
	return circles

def cutImg(name,center):
	img = cv2.imread(photodir+name,3)
	#cimg = img[centerlist[index][0] - clipsize[0]:centerlist[index][0] + clipsize[0],centerlist[index][1] - clipsize[1]:centerlist[index][1] + clipsize[1]]
	cimg = img[center[1] - clipsize[1]:center[1] + clipsize[1],center[0] - clipsize[0]:center[0] + clipsize[0]]
	print 'center:' + str(center)
	print 'imgsize(before resize):' + str(cimg.shape)
	if outputsize[0] != 0:
		cimg = cv2.resize(cimg,tuple(outputsize),cv2.INTER_AREA)
	cv2.imwrite(outputdir+name,cimg)
	return


if __name__ == '__main__':
	centerlist = []
	namelist = []
	fo = open("namelist.txt")
	if not os.path.exists(outputdir):
		os.mkdir(outputdir)
	for photoname in fo:
		photoname = photoname[0:len(photoname)-1]
		getCenter(photoname)
