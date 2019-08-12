import pandas as pd
import numpy as np
import csv
import shutil
import os.path
from collections import Counter

# CREATE A LIST THAT HAS NUTRIENTS AND PRODUCTS AND BREAK IT DOWN BY DIET!
files = ['Nutrients.csv', 'Products.csv']
dataframes = []

for file in files:
     dataframes.append(pd.read_csv(file, low_memory = False))
#    print(dataframes)
     if 'Nutrient_name' in dataframes:
         print('OOOOH YEAH')





file1 = ['Nutrients.csv']
file2 =  ['Products.csv']

with open("outfile", errors = 'ignore') as fw:
    writer = csv.writer(fw)
    for file in file2:
        with open(file) as csvfile:
            info = csv.reader(csvfile, delimiter=',')
            info_types = []
            records = 0
            for row in info:
                print(row[2])
#MAYBE SEPERATE THE FILES? IT MAY MAKE LIFE A LOT EASIER?
