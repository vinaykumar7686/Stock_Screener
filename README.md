# Stock_Screener
Stock Screener to compute the profit/loss (entry price – exit price) from a given strategy .

### Objective:
Build a screener on the data sheet attached. 
The strategy workflow is as follows:-
  - The data is of 1 minute granularity, we have to convert it to 15 min.
  - If low of candle is less than previous low we enter short position, with 2 exit criteria’s
      - Exit at end of day
      - Exit if the high of previous candle is broken
      
Compute the profit/loss(entry price – exit price) from this strategy and upload the code on github.

## How to Run?
  - Clone the Repository
  - Install Python 3.x
  - Install requirements.txt by typing "pip install -r requirements.txt" into Command Prompt in working Directory.
  - Run the file main.py.
