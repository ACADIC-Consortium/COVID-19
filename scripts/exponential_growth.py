import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from array import array
import sys
import xlrd
from openpyxl import Workbook
from scipy.integrate import odeint
import csv
#Import the excel file and  only extract the columns labelled:Entity, Code, cases, Days_30. Entity represents the countries, Code, for country codes e.g Canada has code CA, cases represent the reported cases, Days_30 represent the days from when the number of cases first reached 30.
df =pd.read_csv("Covid_cases.csv", usecols=['Entity','Code', 'cases', 'Days_30'])
#only start counting from day 0
df =df[df['Days_30'] >=0]
#decided to drop Code
df=df.dropna(subset=['Code'])
#Drop countries that didn't  have many cases or whose data was not good
df=df.loc[(df['Entity'] !=('Bahamas'))]
df=df.loc[(df['Entity'] !=('Benin'))]
df=df.loc[(df['Entity'] !=('Botswana'))]
df=df.loc[(df['Entity'] !=('Gambia'))]
df=df.loc[(df['Entity'] !=('Kazakhstan'))]
df=df.loc[(df['Entity'] !=('Kyrgyzstan'))]
df=df.loc[(df['Entity'] !=('Latvia'))]
df=df.loc[(df['Entity'] !=('Lebanon'))]
df=df.loc[(df['Entity'] !=('Sao Tome and Principe'))]
df=df.loc[(df['Entity'] !=('Uganda'))]
df=df.loc[(df['Entity'] !=('Andorra'))]
df=df.loc[(df['Entity'] !=('Angola'))]
df=df.loc[(df['Entity'] !=('Came Verde'))]
df=df.loc[(df['Entity'] !=('Nicaragua'))]
df=df.loc[(df['Entity'] !=('Sri Lanka'))]
df=df.loc[(df['Entity'] !=('Tunisia'))]
df=df.loc[(df['Entity'] !=('Western Sahara'))]
df=df.loc[(df['Entity'] !=('Yemen'))]
df=df.loc[(df['Entity'] !=('Djibouti'))]
df=df.loc[(df['Entity'] !=('Guinea Bissau'))]
df=df.loc[(df['Entity'] !=('Cyprus'))]
df=df.loc[(df['Entity'] !=('Maldives'))]
df=df.loc[(df['Entity'] !=('Sierra Leone'))]
#logistic model functon
def diff(f, x, r,k):
    didt=r*f*(1-f/k)
    return didt
#avoid dubmicate of countries name
result_df = df.drop_duplicates(subset=['Entity'], keep='first')
#pick each country
countries=result_df['Entity'].values
c1 = []
c2 = []
c3=[]
c4=[]
c5=[]
RR=[]
temp=[]
R0=[]
tot=[]

D={}
for item in countries:
    print(item)
    dftemp1=df
    df=df.loc[(df['Entity'] == item)]
    xdata=df.Days_30.values
    ydata=df.cases.values
    xdata1=xdata
    ydata1=ydata
    
    if item=='United States':
      ydata=ydata[:39+5]
      xdata=xdata[:39+5]
    elif item=='Algeria':
        ydata=ydata[:15+5]
        xdata=xdata[:15+5]
    elif item=='Australia':
        ydata=ydata[:18+5]
        xdata=xdata[:18+5]
    elif item=='Bulgaria':
       ydata=ydata[:10+5]
       xdata=xdata[:10+5]
    elif  item=='Croatia':
       ydata=ydata[:8+5]
       xdata=xdata[:8+5]
    elif  item=='Canada':
       ydata=ydata[:50]
       xdata=xdata[:50]
    elif  item=='Israel':
       ydata=ydata[:20+5]
       xdata=xdata[:20+5]
    elif  item=='Japan':
       ydata=ydata[:40+5]
       xdata=xdata[:40+5]
    elif  item=='Macedonia':
       ydata=ydata[:10+5]
       xdata=xdata[:10+5]
    elif  item=='Morocco':
       ydata=ydata[:25+5]
       xdata=xdata[:25+5]
    elif  item=='Netherlands':
       ydata=ydata[:25+5]
       xdata=xdata[:25+5]
    elif  item=='Poland':
       ydata=ydata[:25+5]
       xdata=xdata[:25+5]
    elif  item=='Romania':
       ydata=ydata[:25+5]
       xdata=xdata[:25+5]
    elif  item=='Senegal':
       ydata=ydata[:20+5]
       xdata=xdata[:20+5]
    elif  item=='Serbia':
       ydata=ydata[:25+5]
       xdata=xdata[:25+5]
    elif  item=='Somalia':
       ydata=ydata[:25+5]
       xdata=xdata[:25+5]
    elif  item=='Sweden':
       ydata=ydata[:45+5]
       xdata=xdata[:45+5]
    elif  item=='Ukraine':
       ydata=ydata[:30+5]
       xdata=xdata[:30+5]
    else:
       ydata=ydata
       xdata=xdata
    ind = np.argmax(ydata)
    ydata=ydata[:ind+1]
    
    xdata=xdata[0:ind+1]
    x=xdata
    
    D['Days_30'+ str(item)]=xdata
    D['cases'+ str(item)]=ydata
    inf = []
    def curvefit_model(x,a,r,k):
        f0=a
        f = odeint(diff, f0, x, args=(r,k))
        inff=np.zeros(len(f[:,0]))
        inf.append(f[:,0][0])
        inff[0]=ydata[0]
        
        for ii in range(1, len(f[:,0])):
            inff[ii]=f[:,0][ii]-f[:,0][ii-1]
        return inff
    p0=[5,1,10000]
    popt1, pcov1 = curve_fit(curvefit_model, x, ydata, p0)
    a,r,k=popt1
    c1.append(item)
    c5.append(len(xdata))
    c2.append(r)
    R0.append(np.exp(r*4))
    c4.append(k)
    f0=a
    ff = odeint(diff, f0, x, args=(r,k))
    inff1=np.zeros(len(ff[:,0]))
    inff1[0]=ydata[0]
    for ii in range(1, len(ff[:,0])):
        inff1[ii]=ff[:,0][ii]-ff[:,0][ii-1]
    yOut1 =inff1
    residuals1 = ydata- yOut1
    ss_res1 = np.sum(residuals1**2)
    ss_tot1 = np.sum((ydata-np.mean(ydata))**2)
    r_squared1 = 1 - (ss_res1 / ss_tot1)
    RR.append(r_squared1)
    fig, ax=plt.subplots()
    plt.scatter(xdata1[1:],ydata1[1:], c='k',s=18, label='Real data')
    plt.plot(x[1:], yOut1[1:], 'r', linewidth=2, label='Simulated')
    plt.legend(loc='best')
    ax.set_ylabel('Number of cases in '+ str(item), fontsize=18)
    ax.set_xlabel('Days since confirmed cases first reached 30 a day',fontsize=18)
    ax.tick_params(width = 2, direction = "out")
    fig.savefig(item, bbox_inches='tight')
    plt.close()
    df=dftemp1
with open('Data_july28Final.csv', 'w+') as output:
   writer2 = csv.writer(output)
   for key, value in D.items():
       writer2.writerow([key, value])
df3 = pd.DataFrame({'country': c1, 'Days': c5})
writer3=pd.ExcelWriter('Days.xlsx')
df3.to_excel(writer3, sheet_name='data fitting', index=False)
writer3.save()
writer3.close()
df1 = pd.DataFrame({'country': c1, 'Days_since': c5,  'growth_rate': c2, 'carry capacity': c4, 'R squared': RR, 'R0': R0})
writer1=pd.ExcelWriter('data_fitting_results_August11final.xlsx')
df1.to_excel(writer1, sheet_name='data fitting', index=False)
writer1.save()
writer1.close()

df4 = pd.DataFrame({'country': c1, 'daysince': c5})
writer4=pd.ExcelWriter('Days_since.xlsx')
df4.to_excel(writer4, sheet_name='days', index=False)
writer4.save()
writer4.close()
CC2=np.mean(c2)
CC21=np.std(c2)
CC22=min(c2)
CC23=np.mean(RR)
CC24=np.std(RR)
CC25=min(RR)
print('The mean growth rate is :', CC2)
print('The standard deviation of the  growth rate is :', CC21)
print('The min  growth rate is :', CC22 )
print('The mean R squared is :', CC23)
print('The standard deviation of the  R squared is :',  CC24 )
print('The min  R squared is :', CC25)
