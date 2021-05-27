import cv2
import copy
import numpy as np

def quantization(image , div = 1):
    
    image = np.uint8((image / 255) * (div-1)) * int(255/(div-1))

    return image


def main():
    DIV   = 2
    image = cv2.imread("lenna.png")
    image = quantization(image,DIV)
    cv2.imshow("{}".format(DIV),image)
    cv2.waitKey(0)
    cv2.imwrite("{}.png".format(DIV),image)


if __name__ == "__main__":
    main()