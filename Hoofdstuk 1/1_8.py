import cv2
import numpy as np
import matplotlib.pyplot as plt

retval, mask_thresh = cv2.threshold(fgMask, 200, 255, cv2.THRESH_BINARY)