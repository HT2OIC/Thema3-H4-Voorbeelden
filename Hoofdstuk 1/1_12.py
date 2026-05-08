import cv2
import numpy as np
import matplotlib.pyplot as plt

frame_out = frame.copy()
for cnt in large_contours:
    x, y, w, h = cv2.boundingRect(cnt)
    frame_out = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)

cv2.imshow("Frame_final", frame_out)