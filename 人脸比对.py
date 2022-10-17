from email.mime import image
from multiprocessing.connection import wait
from time import sleep
import cv2
import numpy as np
from PIL import Image
from functools import reduce
from PIL import Image
import math,operator
import pyttsx3

import serial



com = serial.Serial('COM7', 9600)
print (com)

def led1():
        success_bytes = com.write('1'.encode())
        print (success_bytes)
def led2():
        success_bytes = com.write('2'.encode())
        print (success_bytes)  
# import serial
# 库
# 人脸识别部分
# 串口
# com = serial.Serial('COM6', 9600)
# 串口
# 变量
flag=6
engine = pyttsx3.init()
# 变量
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(0)
while cap.isOpened():
    flag,frame=cap.read()
    frame = cv2.flip(frame, 1)
    faces=face_cascade.detectMultiScale(frame,1.3,2)
    img=frame
    flag=6
    for(x,y,w,h)in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,247,181),2)
        face_area=img[y:y+h,x:x+w]
        # print(x)
        # print(y)
        # if(x>0 and y>0 and w>0 and h>0):
        #   flag=1 
        # if(flag==1):
        #     success_bytes = com.write('1'.encode())
        #     print (success_bytes)
        #     print("open")    
        
        #     print("open")  
        cv2.putText(img,'people',(x,y-7),3,1.2,(255,0,251),2,cv2.LINE_AA)
    key_pressed=cv2.waitKey(60)
    # print(flag)
    # if(flag==6):
    #         success_bytes = com.write('5'.encode())
    #         print (success_bytes)
    #  success_bytes = com.write('1'.encode())
    #         print (success_bytes)
    #         print("open")
    # print("123",key_pressed)
    if key_pressed==48:
        img=cv2.Canny(img,100,200)
        img=np.dstack((img,img,img))
    if key_pressed==ord("a"):
        
        cv2.imwrite("photo.jpg",img)
        mying=Image.open("photo.jpg")
        imgcrop=mying.crop((x,y,x+w,y+h))
        mying= imgcrop.resize((150,150),Image.ANTIALIAS)
        mying.save("faceout.jpg")
        print("555555555555555555555555")
    cv2.imshow('rlsb_tool',img)
    if key_pressed==ord("s"):
        cv2.imwrite("photo.jpg",img)
        mying=Image.open("photo.jpg")
        imgcrop=mying.crop((x,y,x+w+10,y+h+10))
        mying= imgcrop.resize((150,150),Image.ANTIALIAS)
        mying.save("faceout2.jpg")
        print("555555555555555555555555")
        h1=Image.open("faceout2.jpg").histogram()
        h2=Image.open("faceout.jpg").histogram()
        RMS=math.sqrt(reduce(operator.add,list(map(lambda a,b:(a-b)**2,h1,h2)))/len(h1))
        print("RMS= ",RMS)
        if(RMS>0):
            if(RMS<70):
                print("匹配成功")
                led1()
                engine.say("匹配成功")
                engine.say("颜孙炜欢迎进入寝室")
                engine.runAndWait()
                sleep(2)
                engine.say("重新上锁")
                engine.runAndWait()
                led2()
            else:
                print("匹配失败")
                engine.say("匹配失败")
                
                engine.runAndWait()
    if key_pressed==27:
        break
    x=0
    y=0
    
cap.release()
cv2.destroyAllWindows
# 人脸识别部分