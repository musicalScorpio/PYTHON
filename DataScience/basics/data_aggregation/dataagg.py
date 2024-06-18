
'''
@author : Sam Mukherjee
Here we will learn how to aggregate data using pandas
Book : Python for data Science
'''

orders = [
 (9423517, '2022-02-04', 9001),
 (4626232, '2022-02-04', 9003),
 (9423534, '2022-02-04', 9001),
 (9423679, '2022-02-05', 9002),
 (4626377, '2022-02-05', 9003),
 (4626412, '2022-02-05', 9004),
 (9423783, '2022-02-06', 9002),
 (4626490, '2022-02-06', 9004)
]

details = [
 (9423517, 'Jeans', 'Rip Curl', 87.0, 1),
 (9423517, 'Jacket', 'The North Face', 112.0, 1),
 (4626232, 'Socks', 'Vans', 15.0, 1),
 (4626232, 'Jeans', 'Quiksilver', 82.0, 1),
 (9423534, 'Socks', 'DC', 10.0, 2),
 (9423534, 'Socks', 'Quiksilver', 12.0, 2),
 (9423679, 'T-shirt', 'Patagonia', 35.0, 1),
 (4626377, 'Hoody', 'Animal', 44.0, 1),
 (4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
 (4626412, 'Shirt', 'Volcom', 78.0, 1),
 (9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
 (9423783, 'Shorts', 'Globe', 26.0, 1),
 (4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
 (4626490, 'Sweater', 'Dickies', 56.0, 1)
]

emps = [
 (9001, 'Jeff Russell', 'LA'),
 (9002, 'Jane Boorman', 'San Francisco'),
 (9003, 'Tom Heints', 'NYC'),
 (9004, 'Maya Silver', 'Philadelphia')
]

locations = [
 ('LA', 'West'),
 ('San Francisco', 'West'),
 ('NYC', 'East'),
 ('Philadelphia', 'East')
]



#Load up Oraders and Details

import pandas as pd
df_orders = pd.DataFrame(orders, columns =['OrderNo', 'Date', 'Empno'])
df_details = pd.DataFrame(details, columns =['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])
df_emps = pd.DataFrame(emps, columns =['Empno', 'Empname', 'Location'])
df_locations = pd.DataFrame(locations, columns =['Location', 'Region'])

df_sales = df_orders.merge(df_details).merge(df_emps).merge(df_locations)
#Creating a new Column on the fly
df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
#Filter out columns that you do not need.
df_sales= df_sales[['Date','Empno', 'Region' , 'Location' , 'Item' , 'Total']]
print(df_sales)
df_sales= df_sales[['Date','Region',  'Total']]
#Now I want to group by the items by region and see how much of a regional sales I got
df_date_region = df_sales.groupby(['Date','Region']).sum()
#print(df_date_region)
#print(df_date_region.index.isin( [('2022-02-05', 'West')]))
#Print after filtering
#print(df_date_region [df_date_region.index.isin( [('2022-02-05', 'West')])])
#Slicing just like  tuple
#print (df_date_region[('2022-02-04', 'East'):('2022-02-04', 'West')])
#print(df_date_region['2022-02-04':'2022-02-05'])
#Slicing total East and West by dates
#print(df_date_region.loc[(slice('2022-02-05', '2022-02-06'), slice(None)), :])
#print(df_date_region.loc[(slice('2022-02-05', '2022-02-06'), slice('')), :])
#All total
ps = df_date_region.sum(axis = 0)
print(ps)
ps.name =('All','All')
#New syntax for new panda https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.T.html
df_date_region_total = pd.concat([df_date_region, ps.to_frame().T])
print(df_date_region_total)
print (df_date_region_total[df_date_region_total.index.isin([('All', 'All')])])
print('====')
print(df_date_region.groupby(level=0).sum())
print('====')
#Subtotal by dates

df_subtotal = pd.DataFrame()
for date, date_df  in df_date_region.groupby(level=0):
   df_date_region_total = pd.concat([df_subtotal, date_df])
   ps = date_df.sum(axis=0)
   ps.name = ('All', 'All')
   #print(ps.to_frame().T)
   df_subtotal_with_total = pd.concat([df_date_region_total, ps.to_frame().T])
   df_subtotal = pd.concat([df_subtotal, df_subtotal_with_total])

print(df_subtotal)