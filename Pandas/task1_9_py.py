# -*- coding: utf-8 -*-
"""task1_9.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P_3FASstolOt7PHJO13TF1l6hduHoWjo
"""

import pandas as pd
data=pd.read_csv("/content/drive/My Drive/diamonds.csv")
print("count, minimum, maximum price for each cut of diamonds DataFrame")
print(data.groupby('cut').price.agg(['count','min','max']))