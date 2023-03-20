import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
pd.options.display.float_format = '{:,}'.format
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('G:/Military Expenditure.csv', index_col =[0])
df_with_index = pd.read_csv('G:/Military Expenditure.csv')

df.isnull().sum()
df.info()
df.shape

graph_data = df[df['Type'] == 'Country'].sort_values(by='2018',ascending=False)[['2018']]
graph_data

plt.plot(graph_data["2018"],c ='k')
plt.xticks(rotation =45)

df_india = df_with_index[df_with_index["Name"] == "India"]
df_ind =df_india.drop(["Indicator Name","Code", "Type"], axis =1)
df_ind_graph =df_ind.melt(id_vars=["Name"],
var_name=["Date"],
value_name="Expend").sort_values(by = 'Expend',ascending = False)
df_ind_graph["Date"] = pd.to_datetime(df_ind_graph["Date"])
plt.plot(df_ind_graph['Date'],df_ind_graph['Expend'],c='r')
plt.xlabel("Year")
plt.ylabel("Increase Expend")
plt.title("1963 to 2018 Military Expend increse \n Year wise")
 '''
conclusion
Military expediture Budget increase little bit at 1963 due to india-china after that it
it increses so fast.
'''