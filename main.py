import pandas as pd
import matplotlib
import pprint as pp

avo_df = pd.read_csv('/home/ali/datasets/avocado.csv')
albany_df = avo_df[avo_df['region'] == 'Albany']

# get values to iterate through
dates = albany_df['Date'].unique()
avo_types = albany_df['type'].unique()
transposed_dict = {}

# iterate through tp get all data
for date in dates:
    df = albany_df[albany_df['Date'] == date]
    for avo_type in avo_types:
        print(avo_type)
        df = albany_df[albany_df['Date'] == date]
        df = df[df['type'] == avo_type]
        avg_price = df.iloc[0]['AveragePrice']
        transposed_dict[date] = {'price': avg_price, 'Type': avo_type}

pp.pprint(transposed_dict)



