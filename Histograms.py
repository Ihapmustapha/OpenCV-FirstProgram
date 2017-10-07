import cv2
import numpy as np

#we must impor matplotilb to create our histograms plots
from matplotlib import pyplot as plt

image = cv2.imread('./images/dog.jpg')
histogram = cv2.calcHist([image], [0], None, [265], [0,256])

