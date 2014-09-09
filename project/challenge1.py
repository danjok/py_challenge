__author__ = 'dani'
import pandas as pd
from Timer import Timer
from config import getFilePath

with Timer() as t:
    data = pd.read_csv(getFilePath('bookings', '2'), sep='^', error_bad_lines=False, warn_bad_lines=True)
    l = len(data)

print("=> read: %s s" % t.secs)
print l

#TODO read all lines to check sanity?
#TODO modify for parallel/distributed version

