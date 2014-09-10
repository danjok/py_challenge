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

#Madrid MAD
#Malaga AGP
#Barcelona BCN
codes = ['MAD','AGP','BCN']

res = pd.DataFrame({})
with Timer() as t:
    for code in codes:
        data_per_city = data[data['Destination'] == code]
        filtered_with_index = data_per_city.set_index('Date')
        res[code] = filtered_with_index.groupby(lambda x : x[:7]).count()['Destination']
print "=> Time: %s s" % t.secs
print res

res = pd.DataFrame({})
with Timer() as t:
    for code in codes:
        data_per_city = data[data['Destination'] == code]
        daily = data_per_city.groupby(['Date']).count()
        monthly = daily.groupby(lambda x : x[:7]).sum()
        res[code] = monthly['Destination']
print "=> Time: %s s" % t.secs
print res


