__author__ = 'dani'

basename = '../datasets/'
filenames = ['bookings', 'searches']
magnitude = ['10_6', '']

def getFilePath(type, magnitude):
    return basename + type + '10_' + magnitude + '.csv'