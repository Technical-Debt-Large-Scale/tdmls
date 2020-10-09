### Loading Dataset
import pandas as pd

### Local
df_all_metrics = pd.read_csv('/Users/armandosoaressousa/git/tdmls/tdmls/dataset/Metrics-Tabela1.csv', sep=";")
df_indian_team = pd.read_csv('/Users/armandosoaressousa/git/tdmls/tdmls/dataset/indian_team.csv', sep=";")
df_sweden_team = pd.read_csv('/Users/armandosoaressousa/git/tdmls/tdmls/dataset/sweden_team.csv', sep=";")
df_italy_team = pd.read_csv('/Users/armandosoaressousa/git/tdmls/tdmls/dataset/italy_team.csv', sep=";")
df_usa_team = pd.read_csv('/Users/armandosoaressousa/git/tdmls/tdmls/dataset/usa_team.csv', sep=";")

print('-------------------------------- DataFrames -------------------------------- ') 
print('DataFrames: df_all_metrics, df_indian_team, df_sweden_team, df_italy_team, df_usa_team')
print('---------------------------------------------------------------------------- ') 

import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt

"""### Functions"""

def show_title(content): 
  print('--------------------------------', content, '--------------------------------')   

# Generate a new list with content in sequence
def generate_list(content, size):
    try:
        my_list = []
        seq = 0

        while int(seq) < size:
            item = content + str(seq)
            my_list.append(item)
            seq = int(seq) + 1
    except Exception as e:
        print("type erro:" + str(e))
    return my_list

# Create a new list with tuple(a,b) from two lists
def create_list_of_tuple(list1, list2):
    try:
        new_list = []
        pair = ()
        size = len(list2)
        for i in range(size):
            pair = (list1[i], ) 
            pair += (list2[i], )
            new_list.append(pair)
    except Exception as e:
        print("type erro:" + str(e))
    return new_list

# Create a dictionary {key:value, ...} from two lists
# key = list2[i]
# value = list1[i]
def create_dictionary_from_lists(list1, list2):
    try:
        my_dictionary = {}
        size = len(list2)
        for i in range(size):
            my_dictionary.update({list2[i]:list1[i]})
    except Exception as e:
        print("type erro:" + str(e))
    return my_dictionary
        
# Create a new dictionary based on generate_list and create_dictionary_from_lists
# my_dataset : dataframe
# my_key : key
# column : column from dataframe
def create_dictionary_from_dataset(my_dataset, my_key, column):
    try:
        my_list = generate_list(my_key, len(my_dataset[column].unique()))
        original_list = my_dataset[column].unique()
        my_dictionary = create_dictionary_from_lists(my_list, original_list)
    except Exception as e:
        print("type erro:" + str(e))
    return my_dictionary
 
# Obfuscation
# my_dictionary_from_indian = create_dictionary_from_dataset(df_indian_team, 'Employee-Indian#', 'employeeName')
# Update employeeName with name obfuscated
# df_indian_team.employeeName = df_indian_team.employeeName.map(my_dictionary_from_indian)

# Show all rows from DataFrame
def print_full(myDF):
  try:
    with pd.option_context("display.max_rows", myDF.shape[0]):
      display(myDF)
  except Exception as e:
    print("type erro:" + str(e))

# Show rows with NaN content from DataFrame
def show_rows_with_NaN(myDF):
  try:
    df1 = myDF[myDF.isna().any(axis=1)]
  except Exception as e:
    print("type erro:" + str(e))
  return df1

# Specific convet to DateTime (01 <= Year <= 19)
def convert_to_DateTime(myDF, column):
  try: 
    for i in range(myDF.shape[0]):
      dateAux = myDF.loc[i, column]
      splitDateAux = dateAux.split("/") 
      yearAux = splitDateAux[2]
      year = int(yearAux) + 2000
      date = splitDateAux[0] + "/" + splitDateAux[1] + "/" + str(year)
      myDF.loc[i, column] = datetime.strptime(date, "%m/%d/%Y")
  except Exception as e:
    print("Error: " + str(e))
  return myDF

# Peek up numeric contend with comma and convert to float
def content_comma_to_float(myDF, column):
  try:
    myDF[column] = myDF[column].str.replace(',', '.').astype(float)
  except Exception as e:
    print("Error: " + str(e))
  return myDF

# Peek up content and convert to float
def content_to_float(myDF, column):
  try:
    myDF[column] = myDF[column].astype(float)
  except Exception as e:
    print("Error: " + str(e))
  return myDF

# Delete Character
def delete_character(myDF, column, character):
  try:
    for i in range(myDF.shape[0]):
      oldStr = myDF.loc[i, column]
      newStr = oldStr.replace(character, "")
      myDF.loc[i, column] = newStr;
  except Exception as e:
    print("Error: " + str(e))
  return myDF

def convert_int_to_string(myDF, column):
  try:
    myDF[column] = myDF[column].astype(str)
  except Exception as e:
    print("Error: " + str(e))
  return myDF

"""## Tables

### Original Metrics Table
"""
show_title('df_all_metrics')
df_all_metrics.head()

"""###Converting Data in Metrics Table"""

df_all_metrics = content_to_float(df_all_metrics, 'maturity')
df_all_metrics = content_to_float(df_all_metrics, 'totalDevelopers')
df_all_metrics = content_to_float(df_all_metrics, 'complexityPoints')
df_all_metrics = content_comma_to_float(df_all_metrics, 'technicalDebt')
df_all_metrics = content_comma_to_float(df_all_metrics, 'taskScaling')
df_all_metrics = content_comma_to_float(df_all_metrics, 'taskGlobalDistance')

df_all_metrics = convert_to_DateTime(df_all_metrics, "start")
df_all_metrics = convert_to_DateTime(df_all_metrics, "end")

df_all_metrics = delete_character(df_all_metrics, "leadTime", "d")
df_all_metrics = content_to_float(df_all_metrics, 'leadTime')

df_all_metrics.info()

df_all_metrics.describe()

df_all_metrics.location.unique()

"""### Metrics Table Complete"""

print_full(df_all_metrics)

df_all_metrics.uniqueID.unique()

len(df_all_metrics.uniqueID.unique())

df_all_metrics.ID.unique()

len(df_all_metrics.ID.unique())

turkey_item = df_all_metrics.query("location == 'Turkey'")
turkey_item

print('It was removed Turkey item from Table Metrics')
df_all_metrics = df_all_metrics.drop(turkey_item.index)

"""### Statistics of Metrics Table"""

df_all_metrics.describe()

sns.boxplot(x='location', y='technicalDebt', data=df_all_metrics).set_title('Boxplot Distribuition Technical Debt x Location')

sns.lmplot(x='leadTime', y='technicalDebt', data=df_all_metrics)

sns.lmplot(x='complexityPoints', y='technicalDebt', data=df_all_metrics)

sns.lmplot(x='maturity', y='technicalDebt', data=df_all_metrics)

ax = sns.regplot(x="maturity", y="technicalDebt", data=df_all_metrics)

sns.lmplot(x='maturity', y='taskGlobalDistance', data=df_all_metrics)

ax = sns.regplot(x="maturity", y="taskGlobalDistance", data=df_all_metrics)

sns.lmplot(x='technicalDebt', y='taskGlobalDistance', data=df_all_metrics)

# Basic correlogram
show_title('Basic correlogram to df_all_metrics')
sns.pairplot(df_all_metrics)
plt.show()

"""### Columns Normalized"""

df_indian_team.columns

"""### Indian Team Table"""

df_indian_team.columns = ['taskID', 'employeeID', 'employeeName', 'team', 'role', 'experienceYears']
df_indian_team.head()

"""**Adding new column 'country'**"""

df_indian_team['country'] = 'Indian'

"""**General information**"""

df_indian_team.info()

"""### Indian Team Table Complete"""
show_title('df_indian_team')
print_full(df_indian_team)

"""### Sweden Team Table"""

df_sweden_team.columns = ['taskID', 'employeeID', 'employeeName', 'team', 'role', 'experienceYears']
df_sweden_team.head()

"""**Adding new column country**"""

df_sweden_team['country'] = 'Sweden'

"""**General Information**"""

df_sweden_team.info()

"""### Sweden Table Complete"""
show_title('df_sweden_teamd')
print_full(df_sweden_team)

"""### Italy Team Table"""

df_italy_team.columns = ['taskID', 'employeeID', 'employeeName', 'team', 'role', 'experienceYears']
df_italy_team.head()

"""**Adding new column country**"""

df_italy_team['country'] = 'Italy'

"""**General Information**"""

df_italy_team.info()

"""### Italy table complete"""
show_title('df_italy_team')
print_full(df_italy_team)

"""### USA Team Table"""

df_usa_team.columns = ['taskID', 'employeeID', 'employeeName', 'team', 'role', 'experienceYears']
df_usa_team.head()

"""**Adding new column country**"""

df_usa_team['country'] = 'USA'

"""**General Information**"""

df_usa_team.info()

"""### USA Table Complete"""
show_title('df_usa_team')
print_full(df_usa_team)

"""### All Team Concatenated"""

frames = [df_indian_team, df_sweden_team, df_italy_team, df_usa_team]

## Concat all teams (Indian, Sweden, Italy, USA) in the same dataframe
df_all_teams = pd.concat(frames)

df_all_teams

df_all_teams.info()

"""**Reseting the index of new DataFrame Concatenated**"""

## Reset index
df_all_teams.reset_index(drop=True, inplace=True)

"""### All Team Table Concatenated Complete"""

df_all_teams.describe()
show_title('df_all_teams')
print_full(df_all_teams)

df_all_teams.team.unique()

df_all_teams.role.unique()

# Show rows with content in Developer, Developers
show_title('Role in [Developers]')
print_full(df_all_teams.query("role in ['Developers']"))

df_all_teams.iloc[df_all_teams.query("role in ['Developers']").index[0]].role = 'Developer'

df_all_teams.role.unique()

"""### Missing Values"""

df_all_teams_NaN = show_rows_with_NaN(df_all_teams)
df_all_teams_NaN

print("Amount of rows with NaN is {}".format(len(df_all_teams_NaN)))

df_all_teams.isnull().sum()

"""```
# This is formatted as code
```

## Data Cleaning and Data Transformation
"""
show_title('Data Cleaning and Data Transformation')
# Rows with NaN content
df_all_teams_NaN.index

# New DataFrame without NaN content
df_all_teams_cleaned = df_all_teams.drop(df_all_teams_NaN.index)
df_all_teams_cleaned.head(10)

"""**Converting String Numeric field to float**"""

df_all_teams_cleaned['experienceYears'] = df_all_teams_cleaned['experienceYears'].str.replace(',', '.').astype(float)
show_title('df_all_teams_cleaned')
print_full(df_all_teams_cleaned)

df_all_teams_cleaned.info()

df_all_teams_cleaned.taskID.unique()

"""**Amount of Diferent taskID**"""

len(df_all_teams_cleaned.taskID.unique())

df_all_teams_cleaned.taskID.value_counts()

"""### Group by TaskID"""

df_all_teams_cleaned_byTaskID = df_all_teams_cleaned.groupby(['taskID']).mean()
df_all_teams_cleaned_byTaskID.sort_values(by=['experienceYears'])

"""## Statistics

### experienceYears
"""

df_all_teams_cleaned.describe()

df_all_teams_cleaned.experienceYears.plot(kind='hist',subplots=True,sharex=True,sharey=True,title='Histogram Experience by Country')

"""### experienceYears by country"""

mean_experienceYears_by_country = df_all_teams_cleaned.groupby("country").mean()['experienceYears']
mean_experienceYears_by_country

sns.boxplot(mean_experienceYears_by_country).set_title('Boxplot Mean Development Experience Year by Country')
plt.show()
sns.boxplot(x='country', y='experienceYears', data=df_all_teams_cleaned).set_title('Boxplot Development Experience Year by Country')
plt.show()
