import cv2
import copy
import numpy as np

def main():
    image = cv2.imread("./lenna.png")
    cv2.imshow("test",image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
