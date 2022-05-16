from ImageEditor import *
from threading import Thread
import threading
import time
#10500


def fill():
    imgList=[]
    for i in range(10100):
        imgList.append(ImageEditor("image.jpg"))
    return imgList

def main():
    
    imgList=fill()
    print("MAIN")
    i=0
    start = time.time()
    while(i<10100):
        
        
        
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
        
        
    elapsed = time.time()-start
    print("Finish!\n")
    print("Elapsed time: "+str(elapsed)+" seconds.\n")

def edit(editor,i):
    editor.imageToGray("out"+str(i))

print("Start!\n")

main()
