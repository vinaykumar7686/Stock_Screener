import pandas as pd

def calc(op, high, low, close):
    '''
    Function to iterate through the lists passed containing dataframe's columns, and find the profit or loss based on the conditions specified.
    '''
    n = len(op)
    curr = 1
    prev = 0
    shortpos = -1
    short = False

    # Find a point when low of candle is less than previous low
    # Now function enters into short position
    # short position is stored and short flag is enabled and then loop is exited.
    while curr<n:
        if low[curr]<low[prev]:
            short = True
            shortpos = curr
            break
        prev = curr
        curr+=1
    
    # If in short position
    if short:

        # Find a point when the high breaks
        #(i.e., High of current is higher than high at short position), if found then break and return (entry price – exit price)
        while curr<n:

            if high[shortpos]<high[curr]:
                return close[curr] - op[0]
            curr+=1

    # Below line runs iff there is no short position or exit condition found
    return close[-1] - op[0]

def main():
    data = pd.read_excel("d:/Programming/Python/Projects/Stock-Screener/NIFTY25JUN2010000PE.xlsx", parse_dates=[['Date', 'Time']]) 

    #convert df index to DataTimeIndex
    data.index = pd.to_datetime(data['Date_Time'] )

    #Resample and aggregate
    Resampled_Data = data.resample('15T').mean()

    # Cleaning NaN Rows
    CnR_Data = Resampled_Data.dropna(axis = 0)

    # Exporting Cleaned and Resampled Sheet
    CnR_Data.to_excel("Cleaned_and_Resampled_Data.xlsx")

    # Getting data date by date
    df = CnR_Data

    # Retrieved all the dates used in the dataframe
    dates = sorted(list(set(df.index.date)))

    print("Date\t\tProfit/Loss\tAmount")
    print("_________________________________________")

    for date in dates[0:]:
        # Extracting Dataframe for a particular day
        data = df.loc[str(date)]

        # Extracting columns of dataframe into list for easy and fast processing
        op, high, low, close = [], [], [], []
        for i in range(data.shape[0]):
            op.append((data.iloc[i])[0])
            high.append((data.iloc[i])[1])
            low.append((data.iloc[i])[2])
            close.append((data.iloc[i])[3])

        # Getting Profit or Loss made by making call to function calc
        pNl = calc(op, high, low, close)

        # Printing fetched results
        if pNl<0:
            print(f"{date} \tLoss \t\t{-round(pNl,2)}")
        elif pNl>0:
            print(f"{date} \tProfit \t\t{round(pNl,2)}")
        else:
            print(f"{date} \tNo Profit or Loss")
        print("_________________________________________")

if __name__ == "__main__":
    main()