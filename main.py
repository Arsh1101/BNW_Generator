from PIL import Image
import os


bnkDir = "./bnk"

def makemydir():
  try:
    os.makedirs(bnkDir)
  except OSError:
    pass


def createBNWImage(dir, fileName):
    image = Image.open(dir + "/" + fileName)
    black_and_white = image.convert("L")
    black_and_white.save(bnkDir + "/" + fileName)


def getDirectory():
    dir = input("Hi please enetr directory address:")
    return dir


def getFiles(dir):
   return os.listdir(dir)


if __name__ == "__main__":
    makemydir()
    dir = getDirectory()
    files = getFiles(dir)
    for fName in files:
       createBNWImage(dir, fName)