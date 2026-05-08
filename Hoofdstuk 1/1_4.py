import cv2
import numpy as np
import matplotlib.pyplot as plt

while True:
    ret, frame = cap.read()
    if frame is None:
        break