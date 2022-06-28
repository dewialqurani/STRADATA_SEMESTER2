#Soal Bagian1
class Pixel():
    def __init__(self,name_pixel,x,y):
        self.name = name_pixel
        self.locate_x = x
        self.locate_y = y
    def moveLeft(self,n):
        self.locate_x -= n
    def moveRight(self,n):
        self.locate_x += n
    def moveForward(self,n):
        self.locate_y += n
    def moveBackward(self,n):
        self.locate_y -= n
    def distance(self,pixel2):
        x1 = self.locate_x
        x2 = pixel2.locate_x
        y1 = self.locate_y
        y2 = pixel2.locate_y
        temp = (((x1-x2)**2)+((y1-y2)**2))**0.5
        return temp
    def display(self):
        print(self.name,": ({},{})".format(self.locate_x,self.locate_y))

pix1 = Pixel("point 1",5,7)
pix2 = Pixel("point 2",6,5)

print("\nBagian1\n")
pix1.display()
pix2.display()
pix1.moveBackward(5)
pix1.display()
jarak = pix1.distance(pix2)
print("jarak =",jarak)
pix2.moveForward(3)
pix2.display()
pix2.moveLeft(1)
pix2.display()
pix2.moveRight(15)
pix2.display()
