# Manual_detection
cnn.h5 is a trained keras model from scratch. I upload here the .h5, you don't need to care about how to train a new model. It's done.
with the modelyou can do classification, to judge if a image belong to P(pitting) class or N(normal) class, the task ist binary classification.
But i wanna show you a further usage with model, for example as a key for object detection.
in the last years, there are a booming development in Deep Learning, specially when it comes to Computer Vision. 
For Object Detection there are firstly sliding windows, then one stage (Yolo,SSD) and two stages (RCNN) detection.
they are all very automated.
I present today a obsolete method to do such a task, with manual detection that you have to choose RoI carefully and slowly. 
But it works anyway
