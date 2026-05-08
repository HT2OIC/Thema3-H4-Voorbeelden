import cv2
import numpy as np
import matplotlib.pyplot as plt

MIN_CONTOUR_AREA = 3000
large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > MIN_CONTOUR_AREA]