import sys                                          # System bindings
import cv2                                          # OpenCV bindings
import numpy as np

class ColorAnalyser():
    def __init__(self, imageLoc):
        i = 10
        self.src = cv2.imread(imageLoc)
        # self.bilateral_blur = cv2.bilateralFilter(self.src,i, i*2, i/2)
        self.bilateral_blur = cv2.GaussianBlur(self.src, (i,i), 0)

        self.colors_count = {}
        self.max_value = 0
        self.max_index = ""
        self.red = 0
        self.green = 0
        self.blue = 0

    def count_colors(self):
        (channel_b, channel_g, channel_r) = cv2.split(self.bilateral_blur)

        channel_b = channel_b.flatten()
        channel_g = channel_g.flatten()
        channel_r = channel_r.flatten()

        for i in xrange(len(channel_b)):
            RGB = str(channel_r[i]) + "," + str(channel_g[i]) + "," + str(channel_b[i])
            if RGB in self.colors_count:
                self.colors_count[RGB] += 1
            else:
                self.colors_count[RGB] = 1

            if i == 0:
                self.max_value = 1
                self.max_index = RGB
            elif channel_r[i] != 0 and channel_b[i] != 0 and channel_g[i] != 0 :
                if self.colors_count[RGB] > self.max_value:
                    self.max_value = self.colors_count[RGB]
                    self.max_index = RGB
                    self.red = channel_r[i]
                    self.green = channel_g[i]
                    self.blue = channel_b[i]

    def modifyBackground(self):
        rows, column, channel = self.bilateral_blur.shape
        for i in xrange(rows):
            for j in xrange(column):
                if self.bilateral_blur.item(i, j, 0) == self.blue and self.bilateral_blur.item(i, j, 1) == self.green and self.bilateral_blur.item(i, j, 2) == self.red:
                    self.bilateral_blur[i, j] = [0, 0, 0]
                    self.src[i, j] = [0, 0, 0]

    def main(self):
        if (self.src == None):
            print "No image data. Check image location for typos"
        else:
            self.count_colors()
            # self.modifyBackground()

            cv2.imshow("blur", self.bilateral_blur)
            key = cv2.waitKey(0)
            if key == 27:
                cv2.destroyAllWindows()


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print "error: syntax is 'python main.py /example/image/location.jpg'"
    else:
        Analyser = ColorAnalyser(sys.argv[1])
        Analyser.main()
