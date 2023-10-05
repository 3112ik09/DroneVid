# Computer Vision Assignment: 

<hr>

## Taks 1: Dedect Lane.
### SCNN 
* Resources : https://github.com/XingangPan/SCNN#Testing , 
* Weights : https://drive.google.com/open?id=1Wv3r3dCYNBwJdKl_WPEfrEOt-XGaROKu
  <pre>
  Used : vgg_SCNN_DULR_w9.t7 is a pre-trained model for lane detection in unstructured environments . 
  trained on dashbord footage. 
  Input Size (600 , 288)
  </pre>
  

### U2Net
https://github.com/xuebinqin/U-2-Net
<pre>
Work : Trained U2Net on Lane Detection for Carla Driving Simulator
Trained models with different loss function , optimizer , batchsize ....etc
Loss Function : BCE , IOU , Die Loss
</pre>

<hr>

## Binary Segmentation Mask Build.
1. Navigate to vgg anotator app to make segmentation.  https://www.robots.ox.ac.uk/~vgg/software/via/
2. Use the Coco format / CSv file to make a binary mask using the polygon dimentions.


<hr>

## Task 2: Dedect Movement

### Yolov8-Deepsort
* https://github.com/ultralytics/ultralytics
<pre>
YOLO DeepSORT object tracking is a combination of two state-of-the-art algorithms: YOLO (You Only Look Once) object detection and DeepSORT object tracking. 
To run git clone above repo.
Place predict.py inside yolo/v8/dedect 
Run script command. 
</pre>


