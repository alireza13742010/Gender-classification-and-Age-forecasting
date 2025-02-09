# -*- coding: utf-8 -*-
"""age_and_gender_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/121qTiA7xIMtFze5mgv4d62DB_hrFWlTv
"""

import os
if not os.path.exists(os.path.join("runs", "predict")):
    os.makedirs(os.path.join("runs", "predict"))

from predict import AgeEstimator
import torch
import matplotlib.pyplot as plt
filename = "/content/gettyimages-1055658634-612x612.jpg"
model = AgeEstimator(weights = "/content/drive/MyDrive/weights.pt")
predicted_image = model.predict(filename)
plt.figure(figsize = (10,8))
plt.imshow(predicted_image)