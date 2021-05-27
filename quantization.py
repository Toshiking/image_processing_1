import cv2
import copy
import numpy as np

def quantization(image , div = 1):
    
    for i in range(0,256,int(256/div)):
        image[:,i*4:i*4+int(256/div)*4,2] = i

    return image


def main():
    DIV   = 2
    image = np.zeros((100,255*4,3)).astype("uint8")
    imaeg = quantization(image,DIV)
    cv2.imshow("{}".format(DIV),image)
    cv2.waitKey(0)
    cv2.imwrite("{}.png".format(DIV),image)


if __name__ == "__main__":
    main()