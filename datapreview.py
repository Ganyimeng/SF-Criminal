# coding = utf-8
import numpy as np
import pandas as pd
def upsampling(data,scale):
    temp = []
    for i in range(int(scale)):
        temp.append(data)
    return pd.concat(temp)

def sampling(data):
    avr = 22514
    max = 174900
    min = 6
    data_in_crimes = []
    for key in numCrimes.keys():
        temp = data[data.Category == key]
        num = temp.shape[0]
        if num <avr:
            data_in_crimes.append(upsampling(temp,np.sqrt(avr/num)))
        else:
            data_in_crimes.append(temp.sample(frac = np.sqrt(1.0*avr/num)))
    return pd.concat(data_in_crimes)

# train = pd.read_csv('..\\train.csv', parse_dates=['Dates'])
# test = pd.read_csv('..\\test.csv', parse_dates=['Dates']).dropna(how='any')
numCrimes = {'KIDNAPPING': 2341,
             'WEAPON LAWS': 8555,
             'SECONDARY CODES': 9985,
             'WARRANTS': 42214,
             'PROSTITUTION': 7484,
             'EMBEZZLEMENT': 1166,
             'PORNOGRAPHY/OBSCENE MAT': 22,
             'FRAUD': 16679,
             'DRIVING UNDER THE INFLUENCE': 2268,
             'VEHICLE THEFT': 53781,
             'ROBBERY': 23000,
             'BURGLARY': 36755,
             'STOLEN PROPERTY': 4540,
             'SUSPICIOUS OCC': 31414,
             'FAMILY OFFENSES': 491,
             'ASSAULT': 76876,
             'FORGERY/COUNTERFEITING': 10609,
             'BAD CHECKS': 406,
             'DRUNKENNESS': 4280,
             'ARSON': 1513,
             'GAMBLING': 146,
             'OTHER OFFENSES': 126182,
             'SUICIDE': 508,
             'RECOVERED VEHICLE': 3138,
             'DRUG/NARCOTIC': 53971,
             'TRESPASS': 7326,
             'LOITERING': 1225,
             'VANDALISM': 44725,
             'MISSING PERSON': 25989,
             'LIQUOR LAWS': 1903,
             'SEX OFFENSES NON FORCIBLE': 148, 'TREA': 6,
             'SEX OFFENSES FORCIBLE': 4388,
             'EXTORTION': 256,
             'BRIBERY': 289,
             'NON-CRIMINAL': 92304,
             'DISORDERLY CONDUCT': 4320,
             'RUNAWAY': 1946,
             'LARCENY/THEFT': 174900}


# hehe = sampling(train)
# print 'the end'