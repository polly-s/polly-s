import statsmodels.api as sm
import numpy as np
import pandas as pd
df=pd.read_csv('data/train_model_data.csv')
columns=['plays','pctmale','age', 'account_age','cluster']
dft=df[columns]
data=dft.dropna()
y1=np.matrix(data['plays']).transpose()
xt=[np.matrix(data[column]).transpose() for column in columns if column !='plays']
x=np.column_stack(xt)
X=sm.add_constant(x)
model=sm.OLS(y1,X)
f=model.fit()
print 'Data: plays'
print 'Coefficients: ',f.params[0:4]
print 'Intercept: ',f.params[4]
print 'P-Values: ',f.pvalues
print 'R-Squared: ',f.rsquared
y2=np.log(np.matrix(data['plays']).transpose())
model=sm.OLS(y2,X)
f=model.fit()
print '\nData: log(plays)'
print 'Coefficients: ',f.params[0:4]
print 'Intercept: ',f.params[4]
print 'P-Values: ',f.pvalues
print 'R-Squared: ',f.rsquared
