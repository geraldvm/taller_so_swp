from PIL import Image

class ImageEditor:
    def __init__(self,filename):
        self.__filename=filename
        self.__image=Image.open(self.__filename)

    def imageToGray(self,filename):
        img=self.__image.convert('L')
        self.__image.close()
        img.save("output/"+filename+".jpg")
        img.close()
        
    def save(self,filename):
        self.__image.save("output/"+filename+".jpg")
