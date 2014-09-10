__author__ = 'dani'
import pandas as pd
from Timer import Timer
from config import getFilePath

cols = {
    'bookings': ['dep_port', 'arr_port', 'pax'],
    'searches': ['Origin', 'Destination'] #Date
}

def readData(label, m):
    with Timer() as t:
        data = pd.read_csv(getFilePath(label, m), sep='^', error_bad_lines=False, warn_bad_lines=True, usecols=cols[label])
        l = len(data)
    print("=> read: %s s" % t.secs)
    print l
    return data

bookings = readData('bookings', '2')
searches = readData('searches', '2')

bookings = pd.read_csv("../datasets/bookings10_6.csv", sep='^', error_bad_lines=False, warn_bad_lines=True, usecols=cols['bookings'])
searches = pd.read_csv("../datasets/searches10_6.csv", sep='^', error_bad_lines=False, warn_bad_lines=True, usecols=cols['searches'])

bookings['dep_port'] = bookings['dep_port'].apply(lambda s : s.strip())
bookings['arr_port'] = bookings['arr_port'].apply(lambda s : s.strip())
searches['Origin'] = searches['Origin'].apply(lambda s : s.strip())
searches['Destination'] = searches['Destination'].apply(lambda s : s.strip())


bookingsGrouped = bookings.groupby(['dep_port', 'arr_port'])[['pax']].sum()
searches['pax'] = 1
searchesGrouped = searches.groupby(['Origin', 'Destination'])[['pax']].sum()

#TODO