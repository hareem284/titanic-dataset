#import matplotlib
import matplotlib.pyplot as plt
#import pandas
import pandas as pd
#importing numpy
import numpy as np
#importing seaborn
import seaborn as sns
#importing statistics
import statistics as st
#reading dataframe
df=pd.read_csv("TIT.csv")
print(df.head())
df.isnull().any()
print(df.dtypes)
meanage=np.mean(df['Age'])
print("the average age was this ta da",meanage)
meanfare=np.mean(df['Fare'])
print("ta da",meanfare)
mediunage=np.median(df['Age'])
print("The median age is ta da!!!!!",mediunage)
medianfare=np.median(df['Fare'])
print("The median fare is ta da!!!!!",medianfare)
#now doing mode
modeage=st.mode(df['Age'])
print("the mode for age is na na na na naaa!!",modeage)
