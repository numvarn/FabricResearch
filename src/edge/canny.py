'''
Created on Jan 4, 2557 BE

@author: Phisan Sookkhee
'''

import cv2

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)

    # just add some colour to edges from original image.
    dst = cv2.bitwise_and(img, img, mask=detected_edges)

    cv2.imshow('Fabrics Image Processing', detected_edges)
    # cv2.imshow('Fabrics Image Processing', dst)

if __name__ == '__main__':
    lowThreshold = 0
    max_lowThreshold = 100
    ratio = 3
    kernel_size = 3

    img = cv2.imread('../images/005.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('Fabrics Image Processing')

    cv2.createTrackbar('Min threshold', 'Fabrics Image Processing', lowThreshold, max_lowThreshold, CannyThreshold)

    # initialization
    CannyThreshold(lowThreshold)

    key = cv2.waitKey(0)

    if key == 27:
        cv2.destroyAllWindows()

    # elif key == ord('s'):
    #     cv2.imwrite('result.jpg',detected_edges)
    #     cv2.destroyAllWindows()




