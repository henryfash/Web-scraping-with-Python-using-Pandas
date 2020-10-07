import pandas as pd

# store the url
page = 'https://www.bbc.com/sport/football/premier-league/table'

# get all the tables from the page
df = pd.read_html(page,header = 0)

# find out the number of tables
print (len(df))

# save the first table
EPL_table = df[0]
# print the table to see if cleaning is necessary
print (EPL_table)

# Cleaning the Table

# get the row index
print (EPL_table.index)
# delete the last row
EPL_table = EPL_table.drop(EPL_table.index[20])

# get the column names
print (EPL_table.columns)
# delete the columns 'unnamed: 1' and 'Form'
EPL_table = EPL_table.drop(['Unnamed: 1', 'Form'], axis=1)

# rename the column 'unnamed: 0'
EPL_table = EPL_table.rename(columns={'Unnamed: 0' : 'Position'})

print (EPL_table)
