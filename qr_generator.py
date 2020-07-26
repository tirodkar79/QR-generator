import qrcode
from PIL import Image
from cv2 import cv2

def name_checker(name):
    if name.endswith(".jpg") or name.endswith(".png"):
        return True
    return False

link = input("Enter your link or data:\t")
name =input("Filename with extension. Eg., abc.jpg:\t")
while True:
    if name_checker(name):
        break
    name =input("Enter proper name:\t")

img = qrcode.make(link)
img.save(name)

img.show()