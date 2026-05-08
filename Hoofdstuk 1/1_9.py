import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)