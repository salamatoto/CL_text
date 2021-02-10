'''
Workflow

* EDA
* KE
* Recommandation System
* Mk Predictive Analysis
* Productionized Wiht Strealit/Flask

==================================
'''
import pandas as pd
import numpy as np
from  sklearn import *
from collections import Counter
import sickitplot as sk
import  matplolib.pyplot as plt
import  seaborn as sns
from warnings import filerwarnings
filtewarnings(action="ignore")

%matplotlib inline 

df = pd.read_csv("namefile.csv")

# Dsitribution of columns
df["col"].value_counts()
 

# to plot the distributation
df["col"].value_counts().plot(kind="bar")

plt.figure(fisize=(10,8))
df["col"].value_counts().plot(kind="pie")
plt.show()

#mothod using seaborn
plt.figure(figsize=(10,12))
sns.countplot(df["col"])
plt.title("any discrbation")
plt.xticks(rotation=42) # to spearate the weight or x
plt.show()

#----------------------------

# to subsceibers per subject use groupby
df.groupby("besic columns")["how many element in besic columns"].sum()  # or counts

df.groupby("besic columns")["how many element in besic columns"].sum().plot(kind="bar")

df.groupby("besic columns")["how many element in besic columns"].sum().plot(kind="pie")

#==================
#totla Number od subsribers
df["col"].sum()
# average of subscribers:
df["col"].mean()

# Which value has highest number od number in columns
df["col"].idxmax()

# how get the location
df.iloc["col"] # index number in datasets

# to use the bar  on sns
plt.figure(figsize=(10,5))
sns.barplot(x="col",y="col1",hue="basic", data=df,ci=None)
plt.show()

#--------------------------------------

# To change value in columns 
df["col"].str.replace("v1|v2", "0")

# To change  the dtypes   like ['12','0']
df["col"] = df["col"].astype(float)

#----
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="col", y="continous", hue="categorical")
plt.show()

# to split the  string like data 2020-02-02T 00:00:00 datatime 

df['col'].str.split("T").str.get(0) # split all value after the forst elemnet
















