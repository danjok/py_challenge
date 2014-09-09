__author__ = 'dani'
import pandas as pd
from Timer import Timer
from config import getFilePath
from GeoBases import GeoBase

geo_o = GeoBase(data='ori_por', verbose=False)
cols = ['year', 'arr_port', 'pax']
with Timer() as t:
    data = pd.read_csv(getFilePath('bookings', '2'), sep='^', error_bad_lines=False, warn_bad_lines=True, usecols=cols)
    l = len(data)
print("=> read: %s s" % t.secs)
print l
print data.columns

filtered_data = data[data.year == 2013]
filtered_data = filtered_data[['arr_port', 'pax']]
#filtered_data has the counter row as index being a DataFrame
#and two series objects: arr_port, pax

#Method 1
#groupby on the arr_port column and then iterate on groups
result = {}
with Timer() as t:
    for arr_port, group in filtered_data.groupby('arr_port'):
        result[arr_port] = group["pax"].sum()
result = sorted(result.items(), key=lambda x:x[1], reverse=True)
print "=> top computation - 1: %s s" % t.secs
#for k,v in result[:10]:
#    print k,v

#Method 2
# groupby on the arr_port column, then access directly to group with pax as a DataFrame
# to execute the sum operation
with Timer() as t:
    groups = filtered_data.groupby('arr_port')
    result = groups[['pax']].sum().sort('pax', ascending = False)
print "=> top computation - 2: %s s" % t.secs
topN = result[:10]
for index, row in topN.iterrows():
     print '%s %d' % (geo_o.get(index.strip(), 'name'), row['pax'])

#Method 3
#use the arr_port as index on rows for the pax Series
with Timer() as t:
    data_with_index = filtered_data.set_index('arr_port')
    groups = data_with_index.groupby(lambda x: x)
    result = groups.sum().sort('pax', ascending = False)
print "=> top computation - 3: %s s" % t.secs
#print result[:10]
