from PIL import Image

class ImageEditor:
    def __init__(self,filename):
        self.__filename=filename
        #self.__image=Image.open(self.__filename)
        #self.__image.close()

    def imageToGray(self,filename):
        image=Image.open(self.__filename)
        img=image.convert('L')
        img.save("output/"+filename+".jpg")
        image.close()
        img.close()
        
    
