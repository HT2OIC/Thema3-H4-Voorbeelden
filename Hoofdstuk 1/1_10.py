import cv2
import numpy as np
import matplotlib.pyplot as plt

contours, hierarchy = cv2.findContours(mask_eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)