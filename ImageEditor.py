from PIL import Image

class ImageEditor:
    def __init__(self,filename):
        self.__filename=filename
        self.__image=Image.open(filename)

    def imageToGray(self,filename):
        self.__image=self.__image.convert('L')
        #self.__image.close()
        self.save(filename)
        self.__image.close()
        
    def save(self,filename):
        self.__image.save("output/"+filename+".jpg")
