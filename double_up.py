import cv2
import copy
import numpy as np

def no_complement(image,amp):
    up_image = np.zeros((image.shape[0]*amp,image.shape[1]*amp,3)).astype('uint8')

    for i in range(0,image.shape[0]*amp, amp):
        for j in range(0,image.shape[1]*amp, amp):
            up_image[i,j] = image[int(i/amp),int(j/amp)]
    return up_image 


def main():
    AMPLITUDE = 2
    image = cv2.imread("./lenna.png")
    
    #補完法なし
    #image = no_complement(image,AMPLITUDE)    

    #最近傍
    #image = cv2.resize(image , (image.shape[1]*AMPLITUDE ,image.shape[0]*AMPLITUDE),cv2.INTER_NEAREST)
    
    #バイリニア
    #image = cv2.resize(image , (image.shape[1]*AMPLITUDE ,image.shape[0]*AMPLITUDE),cv2.INTER_LINEAR)

    #ピクセル領域の関係を利用したリサンプリング
    #image = cv2.resize(image , (image.shape[1]*AMPLITUDE ,image.shape[0]*AMPLITUDE),cv2.INTER_AREA)

    #4 by 4 バイキュービック
    #image = cv2.resize(image , (image.shape[1]*AMPLITUDE ,image.shape[0]*AMPLITUDE),cv2.INTER_CUBIC)

    #8 by 8 ランチョス
    #image = cv2.resize(image , (image.shape[1]*AMPLITUDE ,image.shape[0]*AMPLITUDE),cv2.INTER_LANCZOS4)
    

    cv2.imshow("test",image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
