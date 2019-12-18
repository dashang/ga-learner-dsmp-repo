# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Code starts here

data= pd.read_csv(path)

#histogram
data.Rating.hist()
plt.show()

#cleaning
data=data[data['Rating']<=5]
data.Rating.hist()
plt.show()

#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()
print(total_null)

percent_null = (total_null/data.isnull().count())

missing_data=pd.concat([total_null, percent_null], keys=['Total', 'Percent'],axis=1)

print(missing_data)

data=data.dropna()

total_null_1 = data.isnull().sum()
print(total_null_1)

percent_null_1 = (total_null_1/data.isnull().count())
missing_data_1=pd.concat([total_null_1, percent_null_1], keys=['Total', 'Percent'],axis=1)

print(missing_data_1)
# code ends here


# --------------

#Code starts here

import seaborn as sns

chart=sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
chart.set_xticklabels(rotation=90)
chart.set_titles("Rating vs Category [BoxPlot]")
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import seaborn as sns
#Code starts here

data['Installs'] = [val.replace(',','') for val in data.Installs]
data['Installs'] = [val.replace('+','') for val in data.Installs]
data['Installs'] = [int(val) for val in data.Installs]
print(data['Installs'])

# Create a label (category) encoder object
le = LabelEncoder()
# Fit the encoder to the pandas column
le.fit(data['Installs'])

# Apply the fitted encoder to the pandas column
le.transform(data['Installs']) 
data.Installs = le.fit_transform(data.Installs)
ax = sns.regplot(x="Installs", y="Rating", data=data)
ax.set_title("Rating vs Installs [RegPlot]")
#Code ends here



# --------------
#Code starts here
import seaborn as sns


#print(data.info())
#print(data.head(5))

data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(str).astype(float)

#using Regplot
ax = sns.regplot(x="Price", y="Rating", data=data)
ax.set_title("Rating vs Price [RegPlot]")

#Code ends here


# --------------

#Code starts here

#Observing Variables
print(data['Genres'].unique().size)
print(data['Genres'].unique())

data[['Genres','todelete']] = data['Genres'].str.split(';',expand=True)

#print(data['Genres'].unique())
data = data.drop('todelete',axis= 1)

#group genres
gr_mean = data.loc[:,['Genres','Rating']].groupby(['Genres'], as_index=False).mean() #.apply(lambda x: x.sort_values(['Rating']))
print(gr_mean)
print(gr_mean.describe())

gr_mean=gr_mean.sort_values(by='Rating')
#gr_mean.dtype
print(gr_mean.head(0))
print(gr_mean.tail(0))


#Code ends here


# --------------

#Code starts here

print(data.dtypes)
print(data.head())


data['Last Updated']= pd.to_datetime(data['Last Updated']) 
print(data.dtypes)

max_date = data['Last Updated'].max()
print(max_date)

data['Last Updated Days'] = (max_date-data['Last Updated']).dt.days

sns.regplot(x='Last Updated Days',y='Rating',data=data)
plt.title('Rating vs Last Updated [RegPlot]')
plt.show()

#Code ends here


