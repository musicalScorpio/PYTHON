#Playing with numpy

import numpy as np
jeff_salary = [2700,3000,3000]
nick_salary = [2600,2800,2800]
tom_salary = [2300,2500,2500]
base_salary = np.array([jeff_salary, nick_salary, tom_salary])

jeff_bonus = [500,400,400]
nick_bonus = [600,300,400]
tom_bonus = [200,500,400]
bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])
'''
#Element wise operation
salary_bonus = base_salary + bonus
print(salary_bonus)

#Statistical
max_sal = salary_bonus.max()
print(max_sal)
max_salary_for_any_emp = np.amax(salary_bonus, axis =0)
print(max_salary_for_any_emp)
print(np.mean(max_salary_for_any_emp))
print(np.amax(salary_bonus, axis =1))
#https://NumPy.org/doc/stable/reference/routines.statistics.html.
'''
#Pandas
import pandas as p
data = ['Mom' , 'Dad' , 'Swa' , 'Nikki' , 'Sam']
names_series = p.Series(data)
#print(names)
data_with_custom = p.Series (data, index=[9001,9002,9003,9004,121])
#print(data_with_custom)
#print(data_with_custom[121])
#print(data_with_custom[0:4])
email = ['mom@gmail.com','dad@gmail.com', 'swa@gmail.com','nikki@gmail.com' ,'sam@gmail.com']
email_series = p.Series (email, name='email')
df =p.concat([data_with_custom, email_series], axis=1)

phone = ['891.098.3872','399.876.7192','987.987.8172', '334.987.2839' ,'312.363.7525']
phone_series = p.Series(phone)
df1 =p.concat([names_series, email_series, phone_series], axis=1)
#print(df1)

#Playing with Json data
import json
import pandas as pd
data = [
 {"Empno":9001,"Salary":3000},
 {"Empno":9002,"Salary":2800},
 {"Empno":9003,"Salary":2500}
]
json_data = json.dumps(data)
salary = pd.read_json(json_data)
salary = salary.set_index('Empno')
#print(salary)

import pandas as pd
data = [['9001','Jeff Russell', 'sales'],
        ['9002','Jane Boorman', 'sales'],
        ['9003','Tom Heints', 'sales']]
emps = pd.DataFrame(data, columns = ['Empno', 'Name', 'Job'])
column_types = {'Empno': int, 'Name': str, 'Job': str}
emps = emps.astype(column_types)
emps = emps.set_index('Empno')
#print(emps)

#Combining DataFrames
emps_salary = emps.join(salary)
#print(emps_salary)

new_emp = pd.Series({'Name': 'John Hardy', 'Job': 'sales'}, name = 9004)
emps = emps._append(new_emp)
emps_salary = emps.join(salary)
#print(emps_salary)

#Inner , outer and right
emps_salary = emps.join(salary, how = 'inner')
#print(emps_salary)
emps_salary = emps.join(salary, how = 'outer')
#print(emps_salary)
emps_salary = salary.join(emps, how = 'right')
#print(emps_salary)

#Group by and one - many
import pandas as pd
data = [[2608, 9001,35], [2617, 9001,35], [2620, 9001,139],
        [2621, 9002,95], [2626, 9002,218], [2637, 9003,255], [2701, 9003,232]]
orders = pd.DataFrame(data, columns = ['Pono', 'Empno', 'Total'])
#print(orders)

emps_orders = emps.merge(orders, how='inner', left_on='Empno',  right_on='Empno').set_index('Pono')
#print(emps_orders)
#print(orders.groupby(['Empno'])['Total'].mean())
#print(orders.groupby(['Empno'])['Total'].sum())
#sklearn along with Dataframes
import pandas as pd
df = pd.read_csv('./data_set/sentiment labelled sentences/amazon_cells_labelled.txt', names=['review', 'sentiment'], sep='\t')
#print (df)

#Splitting the Sample Dataset into a Training Set and a Test Set
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
reviews = df['review'].values
sentiments = df['sentiment'].values
#Randomly pick a train dataset
reviews_train, reviews_test, sentiment_train, sentiment_test = train_test_split(reviews, sentiments,  test_size=0.2, random_state=500)

vectorizer = CountVectorizer()
vectorizer.fit(reviews)
X_train = vectorizer.transform(reviews_train)
X_test = vectorizer.transform(reviews_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, sentiment_train)
accuracy = classifier.score(X_test, sentiment_test)
print("Accuracy:", accuracy)

#make predictions fo rnew data
new_reviews = ['Old version of python is horrible', 'Very good effort, but not five stars', 'Clear and concise']
X_new = vectorizer.transform(new_reviews)
print(classifier.predict(X_new))



















