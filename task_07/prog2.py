import matplotlib.pyplot as plt
import pandas as pd
import sys 
from pandas import DataFrame, read_csv

ratings=pd.read_table('./ratings.dat',header=None,delimiter='::',names=['UserID','MovieID','Rating','Timestamp'])
movies=pd.read_table('./movies.dat',header=None,delimiter='::',names=['MovieID', 'Title', 'Genres'])
users=pd.read_table('./users.dat',header=None,delimiter='::',names=['UserID','Gender','Age','Occupation','Zip-Code'])

tab1=ratings[['MovieID','Rating']]
tab2=movies[['MovieID','Title']]
tab1=tab1.merge(tab2, how = 'left', on = 'MovieID')
tab1=tab1[['Title', 'Rating']]
tab3=tab1.groupby('Title', as_index = False)
tab1=tab3.mean()
i=0
c=len(tab1)
tab4=[tab1['Title'][i] for i in range(c) if tab1['Rating'][i] == tab1['Rating'].max()]
DataFrame(tab4, columns = ['Films'])


