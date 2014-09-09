__author__ = 'dani'
import pandas as pd
from Timer import Timer

with Timer() as t:
    data = pd.read_csv('../datasets/bookings10_6.csv', sep='^', error_bad_lines=False, warn_bad_lines=True)
    l = len(data)
    
print("=> read: %s s" % t.secs)
print l