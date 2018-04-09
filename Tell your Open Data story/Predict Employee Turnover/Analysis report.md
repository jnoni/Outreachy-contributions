# Predict Employee Turnover With Python

For the purpose of analysis, I have used python scikit-learn library for basic functions.

## Data Preprocessing

In the dataset, each row represents an employee; each column contains employee attributes:

* satisfaction_level (0–1)
* last_evaluation (Time since last evaluation in years)
* number_projects (Number of projects completed while at work)
* average_monthly_hours (Average monthly hours at workplace)
* time_spend_company (Time spent at the company in years)
* Work_accident (Whether the employee had a workplace accident)
* left (Whether the employee left the workplace or not (1 or 0))
* promotion_last_5years (Whether the employee was promoted in the last five years)
* sales (Department in which they work for)
* salary (Relative level of salary)

```python
import pandas as pd
hr = pd.read_csv('HR.csv')
col_names = hr.columns.tolist()
print("Column names:")
print(col_names)
print("\nSample data:")
hr.head()
```

```
Column names:
['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'left', 'promotion_last_5years', 'sales', 'salary']
```

Table is as follows:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Predict%20Employee%20Turnover/plots/1.PNG)

Rename column name from “sales” to “department”

```python
hr=hr.rename(columns = {'sales':'department'})
```

The type of the column can be found out as follows:

```python
hr.dtypes
```

```
satisfaction_level       float64
last_evaluation          float64
number_project             int64
average_montly_hours       int64
time_spend_company         int64
Work_accident              int64
left                       int64
promotion_last_5years      int64
department                object
salary                    object
dtype: object
```

Data is pretty clean, no missing values:

```python
hr.isnull().any()
```

```
satisfaction_level       False
last_evaluation          False
number_project           False
average_montly_hours     False
time_spend_company       False
Work_accident            False
left                     False
promotion_last_5years    False
department               False
salary                   False
dtype: bool
```

The data contains 14,999 employees and 10 features.

```python
hr.shape
```

```
(14999, 10)
```
The “left” column is the outcome variable recording 1 and 0. 1 for employees who left the company and 0 for those who didn’t.

The department column of the dataset has many categories and we need to reduce the categories for a better modeling. The department column has the following categories:

```python
hr['department'].unique()
```

```
array(['sales', 'accounting', 'hr', 'technical', 'support', 'management',
       'IT', 'product_mng', 'marketing', 'RandD'], dtype=object)
```

Let us combine “technical”, “support” and “IT” these three together and call them “technical”.

```python
import numpy as np
hr['department']=np.where(hr['department'] =='support', 'technical', hr['department'])
hr['department']=np.where(hr['department'] =='IT', 'technical', hr['department'])
```

After the change, this is how the department categories look:

```python
print(hr['department'].unique())
```

```
['sales' 'accounting' 'hr' 'technical' 'management' 'product_mng'
 'marketing' 'RandD']
```

## Data Exploration

First of all, let us find out the number of employees who left the company and those who didn’t:

hr['left'].value_counts()
0    11428
1     3571
Name: left, dtype: int64

There are 3571 employees left and 11428 employees stayed in our data.

Let us get a sense of the numbers across these two classes:

```python
hr.groupby('left').mean()
```

Table is as follows:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Predict%20Employee%20Turnover/plots/2.PNG)

Several observations:

* The average satisfaction level of employees who stayed with the company is higher than that of the employees who left.
* The average monthly work hours of employees who left the company is more than that of the employees who stayed.
* The employees who had workplace accidents are less likely to leave than that of the employee who did not have workplace accidents.
* The employees who were promoted in the last five years are less likely to leave than those who did not get a promotion in the last five years.

We can calculate categorical means for categorical variables such as department and salary to get a more detailed sense of our data like so:

```python
hr.groupby('department').mean()
```

Table:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Predict%20Employee%20Turnover/plots/3.PNG)

```python
hr.groupby('salary').mean()
```

Table:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Predict%20Employee%20Turnover/plots/4.PNG)

## Data Visualization

Let us visualize our data to get a much clearer picture of the data and the significant features.

### Bar chart for department employee work for and the frequency of turnover

```python
%matplotlib inline
import matplotlib.pyplot as plt
pd.crosstab(hr.department,hr.left).plot(kind='bar')
plt.title('Turnover Frequency for Department')
plt.xlabel('Department')
plt.ylabel('Frequency of Turnover')
plt.savefig('department_bar_chart')
```

Plot:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Predict%20Employee%20Turnover/plots/5.PNG)

Observation: It is evident that the frequency of employee turnover depends a great deal on the department they work for. Thus, department can be a good predictor of the outcome variable.

### Bar chart for employee salary level and the frequency of turnover

```python
table=pd.crosstab(hr.salary, hr.left)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Salary Level vs Turnover')
plt.xlabel('Salary Level')
plt.ylabel('Proportion of Employees')
plt.savefig('salary_bar_chart')
```

Plot:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Predict%20Employee%20Turnover/plots/6.PNG)

The proportion of the employee turnover depends a great deal on their salary level; hence, salary level can be a good predictor in predicting the outcome.

Histograms are often one of the most helpful tools we can use for numeric variables during the exploratory phrase.

### Histogram of numeric variables

```python
num_bins = 10

hr.hist(bins=num_bins, figsize=(20,15))
plt.savefig("hr_histogram_plots")
plt.show()
```

Plot:

![alt text](https://github.com/Rupal-IIITD/Outreachy-contributions/blob/master/Tell%20your%20Open%20Data%20story/Predict%20Employee%20Turnover/plots/7.PNG)

