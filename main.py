from ImageEditor import *
from threading import Thread
import threading

#10500


def fill():
    imgList=[]
    for i in range(10500):
        imgList.append(ImageEditor("image.jpg"))
        edit(imgList[i],i)
    return imgList

def main():
    imgList=fill()
    print(len(imgList))
    i=0
    while(i<10500):
        t0=Thread(target=edit, args=(imgList[i],i,))
        t1=Thread(target=edit, args=(imgList[i+1],i+1,))
        t2=Thread(target=edit, args=(imgList[i+2],i+2,))
        t3=Thread(target=edit, args=(imgList[i+3],i+3,))
        t4=Thread(target=edit, args=(imgList[i+4],i+4,))
        t5=Thread(target=edit, args=(imgList[i+5],i+5,))
        t6=Thread(target=edit, args=(imgList[i+6],i+6,))
        t7=Thread(target=edit, args=(imgList[i+7],i+7,))
        t8=Thread(target=edit, args=(imgList[i+8],i+8,))
        t9=Thread(target=edit, args=(imgList[i+9],i+9,))
        t0.start()
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        i+=10
        
    print("Finish")

def edit(editor,i):
    editor.imageToGray("out"+str(i))



main()