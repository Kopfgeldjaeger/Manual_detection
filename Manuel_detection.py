# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:51:36 2020

@author: Yefeng Xia
"""


import glob
import cv2
import os
import numpy as np

img_dir = r"C:\Users\Yefeng Xia\Desktop\KGT_test" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*.jpg')
files = glob.glob(data_path)
fontScale1 = 2
fontScale2 = 2
color1 = (255, 0, 0)
color2 = (0, 0, 255)
thickness = 2
from keras.models import load_model

os.chdir(r"C:\Users\Yefeng Xia\Desktop\KGT_test")
test_cnn= load_model('cnn.h5')
CATEGORIES = ['N','P']

def on_mouse (event,x,y,flags,param):
    global drawing, x_, y_ , x__, y__ 
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_ ,y_ = x, y
        x__,y__ = x_+100, y+100        
        cv2.rectangle(img,(x_-3,y_-3),(x__+3,y__+3),(0,255,0),3)
        
    crop = img[y_:y__,x_:x__]
    #test = img_to_array(load_img(crop, target_size=(100,100)))
    test= np.array(crop)
    test = np.expand_dims(test, axis=0)
    test_scaled = test.astype('float32')
    test_scaled /=255
    
    if event ==cv2.EVENT_LBUTTONUP:
        drawing = True
        font = cv2.FONT_HERSHEY_SIMPLEX 
        org = (x_, y_) 
        
        prediction = test_cnn.predict(test_scaled, verbose=0)
        pred_name = CATEGORIES[np.argmax(prediction)]
        if pred_name == 'N' :
            cv2.putText(img, 'N', org, font,  
                   fontScale1, color1, thickness, cv2.LINE_AA) 
            cv2.rectangle(img,(x_-3,y_-3),(x__+3,y__+3),color1,3)
        elif pred_name == 'P' : 
            cv2.putText(img, 'P', org, font,  
                   fontScale2, color2, thickness, cv2.LINE_AA)
            cv2.rectangle(img,(x_-3,y_-3),(x__+3,y__+3),color2,3)
      


for f1 in files:
    img = cv2.imread(f1)
    #img= cv2.resize(img,(960,540))
    
    drawing = False
    x_, y_ = 0, 0
    x__, y__ = 100, 100
    cv2.namedWindow ('original',cv2.WINDOW_NORMAL)
    cv2.resizeWindow("original", 800, 800) 
    cv2.setMouseCallback('original',on_mouse) 
   
    while True:
        cv2.imshow("original",img)
      
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
cv2.waitKey(0)
cv2.destroyAllWindows()