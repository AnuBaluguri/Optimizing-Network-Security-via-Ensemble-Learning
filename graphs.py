# -*- coding: utf-8 -*-
"""Graphs.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ubd8CMSv0TIiRSgWoGYzKazoKaQQPqL2
"""

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive

from google.colab import drive
drive.mount('/content/drive')

# Assuming your CSV file path is correct (replace with yours)
data_path = '/content/drive/MyDrive/NID_data (1).csv'
data = pd.read_csv(data_path)

# Create subplots for the specified columns
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot histogram for 'duration'
axes[0, 0].hist(data['duration'], bins=30, color='#1f77b4', edgecolor='#1f77b4')
axes[0, 0].set_title('duration')
axes[0, 0].set_xlabel('duration')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].grid(True)

# Plot histogram for 'src_bytes'
axes[0, 1].hist(data['src_bytes'], bins=30, color='#1f77b4', edgecolor='#1f77b4')
axes[0, 1].set_title('src_bytes')
axes[0, 1].set_xlabel('src_bytes')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].grid(True)

# Plot histogram for 'dst_bytes'
axes[1, 0].hist(data['dst_bytes'], bins=30, color='#1f77b4', edgecolor='#1f77b4')
axes[1, 0].set_title('dst_bytes')
axes[1, 0].set_xlabel('dst_bytes')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(True)

# Plot histogram for 'serror_rate'
axes[1, 1].hist(data['serror_rate'], bins=30, color='#1f77b4', edgecolor='#1f77b4')
axes[1, 1].set_title('serror_rate')
axes[1, 1].set_xlabel('serror_rate')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].grid(True)

# Adjust layout
plt.tight_layout()
plt.show()