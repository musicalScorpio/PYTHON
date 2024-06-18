

orders_2022_02_04 = [
 (9423517, '2022-02-04', 9001),
 (4626232, '2022-02-04', 9003),
 (9423534, '2022-02-04', 9001)
]
orders_2022_02_05 = [
 (9423679, '2022-02-05', 9002),
 (4626377, '2022-02-05', 9003),
 (4626412, '2022-02-05', 9004)
]
orders_2022_02_06 = [
 (9423783, '2022-02-06', 9002),
 (4626490, '2022-02-06', 9004)
]

#Combine all the list

orders = orders_2022_02_06 +orders_2022_02_05+orders_2022_02_04
print(orders )

#Combining maps
extra_fields_9423517 = {
  'ShippingInstructions' : { 'name'   : 'John Silver',
                             'Phone' :  [{ 'type' : 'Office', 'number' : '809-123-9309' },
                                         { 'type' : 'Mobile', 'number' : '417-123-4567' }
                                        ]}
}
order_9423517 = {'OrderNo':9423517, 'Date':'2022-02-04', 'Empno':9001}
#comnined map
map_combined = {**extra_fields_9423517 ,**order_9423517}
print(map_combined)
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
details.append((4626592, 'Shorts', 'Protest', 48.0, 1))
'''
Both lists contain tuples whose first element is an order number. The goal is to find the tuples with matching order numbers, 
merge them into a single tuple, and store all the tuples in a list. Here’s how this is done:
'''
import json
orders_details = []
for o in orders:
  for d in details:
    if d[0] == o[0]:
      #Do not add the first order numner but everything else
      orders_details.append(o + d[1:])

print(json.dumps(orders_details, indent=2))

#orders_details = [[o for o in orders if d[0] == o][0] + d[1:] for d in details]
#print(json.dumps(orders_details, indent=2))
orders_details_right = [[o for o in orders if d[0] in o][0] + d[1:] if d[0] in [o[0] for o in orders]  else (d[0], None, None) + d[1:] for d in details]
print(json.dumps(orders_details_right, indent=2))

#summing
print (sum(pr*qt for _, _, _, _, _, pr, qt in orders_details_right))

#concatenation with numpy
import numpy as np
jeff_salary = [2700,3000,3000]
nick_salary = [2600,2800,2800]
tom_salary = [2300,2500,2500]
base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])
#print(base_salary1)
maya_salary = [2200,2400,2400]
john_salary = [2500,2700,2700]
base_salary2 = np.array([maya_salary, john_salary])
base_salary = np.concatenate((base_salary1, base_salary2), axis=0)
print(base_salary)
new_month_salary = np.array([[3000],[2900],[2500],[2500],[2700]])
base_salary = np.concatenate((base_salary, new_month_salary), axis=1)
print(base_salary)

import pandas as pd
salary_df1 = pd.DataFrame(
    {'jeff': jeff_salary,
     'nick': nick_salary,
     'tom': tom_salary
    })
print(salary_df1)
salary_df1.index = ['June', 'July', 'August']
print(salary_df1)
print(salary_df1.T)

salary_df2 = pd.DataFrame(
    {'maya': maya_salary,
     'john': john_salary
    },
    index = ['June', 'July', 'August']
).T
salary_df = pd.concat([salary_df1.T, salary_df2])
print(salary_df)
salary_df3 = pd.DataFrame(
    {'September': [3000,2800,2500,2400,2700],
     'October': [3200,3000,2700,2500,2900]
    },
    index = ['jeff', 'nick', 'tom', 'maya', 'john']
)
salary_df = pd.concat([salary_df, salary_df3], axis=1)
print(salary_df)
salary_df = salary_df.drop(['September', 'October'], axis=1)
print(salary_df)

#Sort two data frames by dates
df_date_region1 = pd.DataFrame(
 [
  ('2022-02-04', 'East', 97.0),
  ('2022-02-04', 'West', 243.0),
  ('2022-02-05', 'East', 160.0),
  ('2022-02-05', 'West', 35.0),
  ('2022-02-06', 'East', 110.0),
  ('2022-02-06', 'West', 86.0)
 ],
 columns =['Date', 'Region', 'Total']).set_index(['Date','Region'])
print(df_date_region1)

df_date_region2 = pd.DataFrame(
 [
  ('2022-02-04', 'South', 114.0),
  ('2022-02-05', 'South', 325.0),
  ('2022-02-06', 'South', 212.0)
 ],
 columns =['Date', 'Region', 'Total']).set_index(['Date','Region'])
#Hint to keep the data by dates
df_date_region = pd.concat([df_date_region1, df_date_region2]).sort_index(level=['Date','Region'])
print(df_date_region)

print('==========================')
import pandas as pd
df_orders = pd.DataFrame(orders, columns =['OrderNo', 'Date', 'Empno'])
df_details = pd.DataFrame(details, columns =['OrderNo', 'Item', 'Brand',  'Price', 'Quantity'])
str ={'OrderNo': [4626595], 'Item': ['Shorts'],'Brand': ['Protest'],'Price':[ 48.0 ],'Quantity': [1]}
dat_fr = pd.DataFrame.from_dict(str)
df_details = pd.concat ( [df_details , dat_fr])


df_orders_details_right = df_orders.merge(df_details, how='right', left_on='OrderNo', right_on='OrderNo')
print(df_orders_details_right)

print(df_orders_details_right.dtypes)
df_orders_details_right = df_orders_details_right.fillna({'Empno':0}).astype({'Empno':'int64'})
print(df_orders_details_right)
#may to many joins
import pandas as pd
books = pd.DataFrame({'book_id': ['b1', 'b2', 'b3'],
                      'title': ['Beautiful Coding', 'Python for Web Development', 'Pythonic Thinking'],
                      'topic': ['programming', 'Python, Web', 'Python']})
authors = pd.DataFrame({'author_id': ['jsn', 'tri', 'wsn'],
                        'author': ['Johnson', 'Treloni', 'Willson']})

matching = pd.DataFrame({'author_id': ['jsn', 'jsn','tri', 'wsn'],
                           'book_id': ['b1', 'b2', 'b2', 'b3']})

authorship = books.merge(matching).merge(authors)[['title','topic','author']]
print(authorship)










