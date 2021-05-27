import cv2
import copy
import numpy as np

def main():
    image = np.zeros((256,256,3)).astype("uint8")
    image[:,:,0] = 255
    image[:,:,1] = 30  
    image[:,:,2] = 100 
    cv2.imshow("result",image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
