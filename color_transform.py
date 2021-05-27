import cv2
import copy
import numpy as np

def linear(image):
    return image

def linear_2(image , min , max):
    image = np.float32(image)
    image = np.minimum(np.maximum(255/(max - min)*image - 255*min/(max-min),0),255)
    return np.uint8(image)

def non_linear(image):
    image = np.float32(image)
    image = image * image/255
    return np.uint8(image)

def non_linear_2(image):
    image = np.float32(image)
    image = np.sqrt(image/255) * 255
    return np.uint8(image)


def main():
    image = cv2.imread("./lenna.png")
    image = non_linear_2(image)
    cv2.imwrite("linear.png",image)

if __name__ == "__main__":
    main()
