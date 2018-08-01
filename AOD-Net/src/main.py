
'''
In order to update the size of the frame, change the dimension in 
the resize function and also update the DeployT.prototxt file with 
the coresponding entries in the input LAYER of caffe NET. With first input_dim as height and second one as width.
 opencv 3.4
'''

#!/usr/bin/python2.7
import caffe
import time
import cv2
import sys
import numpy as np


def EditFcnProto(templateFile, height, width):
	with open(templateFile, 'r') as ft:
		template = ft.read()
        #print templateFile
        outFile = 'DeployT.prototxt'
        with open(outFile, 'w') as fd:
            fd.write(template.format(height=height,width=width))




def resize(img):
    
    if img.shape[0]>500 and img.shape[1]>500:
        img = cv2.resize(img,(500,500))
    elif img.shape[0]>500 :
        img = cv2.resize(img,(500,img.shape[1]))
    elif img.shape[1]>500:
        img = cv2.resize(img,(img.shape[0],500))
    #cv2.imshow('AOD-net',img2)
    return img

def video_resize():
    v = cv2.VideoCapture('../data/test_/new_delhi.mkv')

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('../data/test_/new_delhi1.avi',fourcc, 20.0, (700,700)) # change this according to the size of frame
    while(v.isOpened()):
        ret, frame = v.read()
        frame = resize(frame)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    v.release()



def contineous_video():
    
    caffe.set_mode_cpu()
    v=cv2.VideoCapture('../data/test_/new_delhi.mkv')
#    templateFile = '/home/ac/AOD-Net/test/test_template.prototxt'
 #   EditFcnProto(templateFile, 300, 300)
    model='AOD_Net.caffemodel'
  
    fps_actual = v.get(cv2.CAP_PROP_FPS)
    print "the actual fps is : ",fps_actual
    
    net = caffe.Net('DeployT.prototxt', model, caffe.TEST)
    frames =120 #compare fps for 2 minutes 
    #while (True):
    start = time.time()
    for i in range(0,frames): 
        ret, frame = v.read()       
        frame = resize (frame)
        
        frame = frame[...,::-1]/255.0#bgr2rgb as caffe supports rgb format
        batchdata = []
        data = frame
        data = data[:, :, ::-1]
        
        data = data.transpose((2, 0, 1))
        batchdata.append(data)
        net.blobs['data'].data[...] = batchdata

        net.forward()
        
        data = net.blobs['sum'].data[0]
        
        data = data.transpose((1, 2, 0))
        data = data[:, :, ::-1]
        data = data[...,::-1]
        cv2.imshow("image" ,data)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #this waitkey stops the fram for the assigned seconds
                break
    end = time.time()
    print ("the fps is after dehazing operation is: {}".format(frames/(end - start)))
    v.release()
    cv2.destroyAllWindows()


def AOD_Net_modify_image(image_matrix): #takes in a matrix and returns a matrix of dehazed image

    caffe.set_mode_cpu()

    frame=image_matrix       
    frame = resize (frame)
    frame = frame[...,::-1]/255.0#bgr2rgb
    height = frame.shape[0]
    width = frame.shape[1]
    templateFile = 'test_template.prototxt'
    EditFcnProto(templateFile, height, width)
    model='AOD_Net.caffemodel'
 
    net = caffe.Net('DeployT.prototxt', model, caffe.TEST)
    batchdata = []
    data = frame
    data = data[:, :, ::-1]#rgbtobgr
    #print net   
        
    data = data.transpose((2, 0, 1))
    batchdata.append(data)
    net.blobs['data'].data[...] = batchdata

    net.forward();
        
    data = net.blobs['sum'].data[0]
        
    data = data.transpose((1, 2, 0))
    data = data[:, :, ::-1]
    data = data[...,::-1]
    data = np.uint8(np.array(data)*255.0) #change the image type to opencv formate
  #  data = data.copy()
    return data 



def AOD_Net_save_the_video():#this doesnt work fine
    
    caffe.set_mode_cpu()
    v=cv2.VideoCapture('../data/test_/new_delhi.mkv')
#    templateFile = '/home/ac/AOD-Net/test/test_template.prototxt'
 #   EditFcnProto(templateFile, 300, 300)
    model='AOD_Net.caffemodel';
    #v=cv2.VideoCapture('/home/ac/AOD-Net/test/haze.mp4')#give the file name
    #fps = v.get(cv2.cv.CV_CAP_PROP_FPS)
    #print "the actual fps is {}".format(fps)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('ouput.avi',fourcc,20.0,(700, 700))
    net = caffe.Net('DeployT.prototxt', model, caffe.TEST);
    
    while (v.isOpened()):
        ret, frame = v.read()       
       # frame = resize (frame1)
        #frame = frame1
        frame = frame[...,::-1]/255.0#bgr2rgb
   
        batchdata = []
        data = frame
        data = data[:, :, ::-1]
        
        data = data.transpose((2, 0, 1))
        batchdata.append(data)
        net.blobs['data'].data[...] = batchdata;

        net.forward();
        
        data = net.blobs['sum'].data[0];
        
        data = data.transpose((1, 2, 0));
        data = data[:, :, ::-1]
        data = data[...,::-1]
        data = np.uint8((np.array(data)*255.0)) 
        data = data.copy()   

        out.write(data)
        cv2.imshow("image" ,data)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #this waitkey stops the fram for the assigned seconds
                break

   
    v.release()
    out.release()







def dehaze_frame(): # this performs dehazing on a frame.
    img = cv2.imread(sys.argv[1])
    img = AOD_Net_modify_image(img)
    cv2.imwrite("dehazed_dust.jpg",img)
	#cv2.imshow("dehazed-image",img)
	#cv2.waitKey(0)    #this waitkey stops the fram for the assigned seconds
#	cv2.destroyAllWindows()
   






def main():
    

#    v=cv2.VideoCapture('/home/ac/AOD-Net/test/new_delhi.mkv')
 #   while (v.isOpened()):
  #      ret, frame1 = v.read()   
   #     print frame1.shape
    #img = cv2.imread(sys.argv[1])
    #img = AOD_Net_modify_image(img)
    #cv2.imshow("dehazed",img)
    #cv2.waitKey(0) & 0xFF
    #cv2.destroyAllWindows()
    #contineous_video()
   # AOD_Net_save_the_video()
    #video_resize()

    dehaze_frame()
if __name__ == '__main__':

    main();


