import pandas as pd
import pandas_datareader.data as web
import numpy as np

#unit data is pulled from here (PAlobby unit database)
units_def = 'https://palobby.com/units/table/defense'

#unit data is read into a list
defensive = pd.read_html(units_def)

#data is then reformatted into a pandas dataframe and assigned to df
df = defensive[0]
#quick clean up removing NaN column
df  = df.dropna(axis = 'columns')

#First test comparing DPS
def test_dps(first,second):
    if first['DPS'] > second['DPS']:
        first_dps = True
        second_dps = False
        print('%s is stronger than %s!' % (first['Name'], second['Name']))

    elif first['DPS'] < second['DPS']:
        first_dps = False
        second_dps = True
        print('%s is stronger than %s!' % (second['Name'], first['Name']))

    elif first['DPS'] == second['DPS']:
        first_dps = True
        second_dps = True
        print('%s and %s are equal in DPS!' % (first['Name'], second['Name']))

    else:
        return('error')


max  = len(df) - 1

tst1 = np.random.randint(max, size = 1, dtype = 'int')
tst2 = np.random.randint(max, size = 1, dtype = 'int')

first = df.iloc[int(tst1)]
second = df.iloc[int(tst2)]

test_dps(first,second)
