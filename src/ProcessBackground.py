import cv2
import numpy as np

KERNEL_SIZE = 3

class ProcessBackground():
    def __init__(self, path):
        self.img = cv2.imread(path)
        self.gray = ''
        self.thresh = ''

    def process(self):
        # convert originale image to gray scale
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # reduce background noise using Gaussian Fillter
        self.blur = cv2.GaussianBlur(self.gray, (KERNEL_SIZE, KERNEL_SIZE), 0)

        # convert to binary image
        ret, self.thresh = cv2.threshold(self.blur, 127, 255, cv2.THRESH_BINARY)

        # bitwise mask and original image
        self.result = cv2.bitwise_and(self.img, self.img, mask=self.thresh)

    def main(self):
        self.process()

        cv2.imshow("theshold image", self.result)
        key = cv2.waitKey(0)
        if key == 27:
            cv2.destroyAllWindows()

if __name__ == '__main__':
    path = '/Users/phisan/Sites/research/Frabics/images/005.jpg'
    process = ProcessBackground(path)
    process.main()



