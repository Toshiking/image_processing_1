import cv2
import copy
import numpy as np

def main():
    image = cv2.imread("./lenna.png")
    print(image.shape)

if __name__ == "__main__":
    main()
