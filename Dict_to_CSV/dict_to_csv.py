__author__ = 'Aayush Bhardwaj'

import csv
from test_sheet import dict
my_dict = dict
with open('mycsvfile.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    for x in range(len(my_dict)):
        le=my_dict[x]
        if 'subtiers' in le.keys():
            continue
        else:
            w = csv.DictWriter(f, le.keys())
            w.writerow(le)