import pandas as pd
import numpy as np
import csv
import shutil
import os.path
from collections import Counter

food = pd.read_csv('Nutrients.csv', 'Products.csv')
print(food.head())
