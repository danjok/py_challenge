__author__ = 'dani'
import pandas as pd
from Timer import Timer
from config import getFilePath

cols = ['Destination', 'Date']
with Timer() as t:
    data = pd.read_csv(getFilePath('searches', '6'), sep='^', error_bad_lines=False, warn_bad_lines=True, usecols=cols)
    l = len(data)
print("=> read: %s s" % t.secs)
print l
print data.columns

#TODO groupby destination, year, month and then count
#new_column with YY-MM
#one plot for each destination

#Madrid MAD
#Malaga AGP
#Barcelona BCN
codes = ['MAD','AGP','BCN']
for code in codes:
    with Timer() as t:
        filtered = data[data['Destination'] == code]
        filtered_with_index = filtered.set_index('Date')
        res = filtered_with_index.groupby(lambda x : x[:7]).count()
    print "=> mean - 1: %s s" % t.secs
    print res
