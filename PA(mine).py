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

#second test comparing HP
def test_hp(first,second):
    if first['HP'] > second['HP']:
        first_hp = True
        second_hp = False
        print('%s has higher HP than %s!' % (first['Name'], second['Name']))

    elif first['HP'] < second['HP']:
        first_hp = False
        second_hp = True
        print('%s has higher HP than %s!' % (second['Name'], first['Name']))

    elif first['HP'] == second['HP']:
        first_hp = True
        second_hp = True
        print('%s and %s are equal in HP!' % (first['Name'], second['Name']))

    else:
        return('error')

# Third test comparing cost
def test_cost(first,second):
    if first['Cost'] > second['Cost']:
        first_cost = True
        second_cost = False
        print('%s has a higher Cost than %s!' % (first['Name'], second['Name']))

    elif first['Cost'] < second['Cost']:
        first_cost = False
        second_cost = True
        print('%s has a higher Cost than %s!' % (second['Name'], first['Name']))

    elif first['Cost'] == second['Cost']:
        first_cost = True
        second_cost = True
        print('%s and %s are equal in Cost!' % (first['Name'], second['Name']))

    else:
        return('error')





max  = len(df) - 1

tst1 = np.random.randint(max, size = 1, dtype = 'int')
tst2 = np.random.randint(max, size = 1, dtype = 'int')

first = df.iloc[int(tst1)]
second = df.iloc[int(tst2)]

test_dps(first,second)
test_hp(first,second)
test_cost(first,second)


#The program needs to do a few things.
# 1. it needs to compare one unit in a class to all others in the same class.
# 2. it needs to create a dataframe of all possible comparisons of units in that class.
# 3. it needs to algorithmically determine the best unit in its class by comparing the 3 main factors
# 4. it also needs to consider cost per health point and other calculations
# 5. it needs to then move on to see if those units are better than units outside of their own class.
