import cv2
import numpy as np
import matplotlib.pyplot as plt

fgMask = backSub.apply(frame)
cv2.imshow('FG Mask', fgMask)