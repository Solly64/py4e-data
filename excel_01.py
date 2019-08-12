import pandas as pd
import numpy as np
import csv
import shutil
import os.path
from collections import Counter

# CREATE A LIST THAT HAS NUTRIENTS AND PRODUCTS AND BREAK IT DOWN BY DIET!
files = ['Nutrients.csv', 'Products.csv']

with open("outfile", errors = 'ignore') as fw:
    writer = csv.writer(fw)
    for file in files:
        with open(file) as csvfile:
            info = csv.reader(csvfile, delimiter=',')
            info_types = []
            records = 0
            for row in info:
                if 'STEAK SAUCE' in row:
                    print('YUMMMMY')
#TRY TO VISULAIZED THE DATA I HAVE
