
import pandas as pd
import numpy as np

from collections import Counter

from builtins import int


def MapClass(read_clients):
    row = read_clients.shape[0]
    col = read_clients.shape[1]
    MissingData = read_clients.fillna("NaN")
    print('Missing Data Filled with NaN is', MissingData)
    FinalData = read_clients.fillna("NaN")
    redOut = []
    Shell = []
    for c in range(0, col):
        dv = 0
        # Comment start
        # This is iterating for every coloumn
        # We are finding the missing data
        # and tring to put some postion value
        # using the function iloc().
        for r in range(1):
            dv = MissingData.iloc[r, c]
        # Comment end

        # Comment Start
        # We are here, only if the tuple (dv) is of type
        # integer or float
        if isinstance(dv, float) or isinstance(dv, int):
            z = []
            a = 0
            i = 0
            mean = 0
            # We are itereating for every row
            # Step 1 :
            # get the list of NaN
            # send it to magic box called reducerclass
            # it gives me redout
            # now take this red out
            # again check the list
            # fill redout in places where there is NaN
            for r in range(0, row - 1):
                i += 1
                # If something is not missing
                # We are adding the position of
                # the valye MissingData.iloc[r, c]
                # to the variable a
                # then we are calulcating the mean.
                # [1,2,3,NaN<7.8>,NaN<7.8>,7]
                # 1 -> 1/1 -> 1
                #  -> 3/2 -> 1.5
                # (1 + 2) + 3 -> 6/3 -> 2
                if MissingData.iloc[r, c] != 'NaN':
                    a += MissingData.iloc[r, c]
                    mean = a / i
                    mean = round(mean, 2)
                else:
                    # if its a Nan
                    # then we append to z which is an array
                    # add the mean which we have right now to the as the missing value
                    z.append(mean) #[3,4]
                    MissingData.iloc[r, c] = mean
                    a += mean

            # if there is no Nan then dont do anything
            if len(z) == 0:
                print('')
            else:
                # else send to reducer class
                redOut = ReducerClass(z) # [3,4]
                # [7.8]

            # if something is NaN, then we put it from reducer output
            # if there is NaN then dont do anything
            for j in range(0, row): # we are iterating the tuple
                if FinalData.iloc[j, c] == 'NaN':
                    FinalData.iloc[j, c] = redOut # Missing DATA to unmissing

        #Comment End

        #Comment Start
        # We are here, only if the tuple (dv) is of type
        # anything other than
        # integer or float
        else:
            i = 0
            d = []
            m = []
            for r in range(0, row):
                i += 1
                if MissingData.iloc[r, c] == 'NaN':
                    MissingData.iloc[r, c] = Shell
                    m.append(Shell)
                    d.append(Shell)
                else:
                    d.append(MissingData.iloc[r, c])
                    Shell = categorical(d)
                    print('The estimated value for this missing index is', Shell)

            # print('The array input is', )
            print('the List of Estimated data is', m)
            Catagory = categorical(m)
            for j in range(0, row):
                # print('Catagory is', Catagory)
                if FinalData.iloc[j, c] == 'NaN':
                    FinalData.iloc[j, c] = Catagory
                    # print('Catagory is', FinalData.iloc[j,c])
                # print('Output file is', FinalData)
        # Comment End

    return FinalData


def ReducerClass(Map_input):
    print('The Reducer Input is', Map_input)
    #     Map_input=list(set(Map_input))
    print('The Count', Counter(Map_input))

    #     print(dict((i, Map_input.count(i)) for i in Map_input))
    # Checking max & min of map_input, basically highest count of a value in the row
    Imputedvalue = max(set(Map_input), key=Map_input.count)
    test = min(set(Map_input), key=Map_input.count)
    if (Imputedvalue == test):
        Imputedvalue = np.median(Map_input)
    print('Value with more confidence:', Imputedvalue)

    return Imputedvalue


def categorical(Cat_input):
    i = 0
    print('The Categorical Input is', Cat_input)
    #     Map_input=list(set(Map_input))
    print('The Count', Counter(Cat_input))
    #     print(dict((i, Map_input.count(i)) for i in Map_input))
    if len(Cat_input) == 0:
        return
    CatFinalval = max(set(Cat_input), key=Cat_input.count)
    print('Value with more confidence:', CatFinalval)
    print(i)
    return CatFinalval


def main():
    read_clients = pd.read_excel(r'C:\CNP_AE_1.xlsx', header=None)
    Missingdata = MapClass(read_clients)
    # print('type is', Missingdata.dtype)
    Missingdata.to_excel(r'D:\CNP_AE_1_OUTput123.xlsx', header=None, index=False)


if __name__ == "__main__":
    main()