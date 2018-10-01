# Info

IROB uses pre-trained model of MobileNet-SSD. The model is conversion of model originally#
implemented on tensorflow framework. The Model was trained on COCO dataset but since
the main focus was on finding person we choose the model that was fine-tuned on PASCAL VOC
dataset, which has only 20 different object classes with one background class. Initially the
implementation was done on caffe on ASUS laptop with Intel(R) Core(TM) i5-6200U CPU,2.30GHz and later deployed on UP-Square 
with Intel(R) Celeron(R) CPU N3350,1.10GHz with and without Intel Movidus NCS.

## The directory contains three implementions of person detection.

**SSD_MobileNet_MovidusAcceleration** - Person Detection inferenencing on Movidus NCS. (to increase frame rate)

**person_detection_mobilenet_SSD** - Person Detection inferenencing on UP-Square with Intel(R) Celeron(R) CPU N3350,1.10GHz without Intel Movidus NCS.

**harcasced** - Traditional method of person detection without CNN approach. 

Apart from that **.caffemodel** and **.prototxt** files are also included in the directory.

## For more details -

COCO dataset - http://cocodataset.org/ 

PASCAL VOC - http://host.robots.ox.ac.uk/pascal/VOC/ 

## Intel Movidus is a edge device with capability to inference caffe and tensorflow models more details can be found here- 

https://software.intel.com/en-us/videos/deploying-image-classifiers-on-intel-movidius-neural-compute-stick 

https://www.youtube.com/watch?v=KuM67WfTXBQ

# Refernece - 

https://www.pyimagesearch.com/2018/02/12/getting-started-with-the-intel-movidius-neural-compute-stick/

https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/

https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/
