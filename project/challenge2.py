__author__ = 'dani'
import pandas as pd
from Timer import Timer
from config import getFilePath

cols = ['year', 'arr_port', 'pax']
with Timer() as t:
    data = pd.read_csv(getFilePath('bookings', '6'), sep='^', error_bad_lines=False, warn_bad_lines=True, usecols=cols)
    l = len(data)
print("=> read: %s s" % t.secs)
print l
print data.columns

filtered_data = data[data.year == 2013]
filtered_data = filtered_data[['arr_port', 'pax']]

result = {}
with Timer() as t:
    for arr_port, group in filtered_data.groupby('arr_port'):
        result[arr_port] = group["pax"].sum()
print "=> top computation: %s s" % t.secs
print result
#TODO sort result

