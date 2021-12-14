import numpy as np
import imutils
import cv2 as cv


class SingleMotionDetector:
    #
    def __init__(self, accumWeight=0.5):
        # stores the accumulated weight factor
        self.accumWeight = accumWeight

        # initialize the background model
        self.bg = None

    def update(self, image):
        # initializes background model if None exists
        if self.bg is None:
            self.bg = image.copy().astype('float')
            return

        # updates background model by accumulating the weighted average
        cv.accumulateWeighted(image, self.bg, self.accumWeight)

    def detect(self, img, tVal=25):
        # creates an image within the absdiff parameter
        delta = cv.absdiff(self.bg.astype("uint8"), img)
        # details a threshold value for detecting motion
        thresh = cv.threshold(delta, tVal, 255, cv.THRESH_BINARY)[1]

