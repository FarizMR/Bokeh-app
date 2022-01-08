#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row, gridplot, column
from bokeh.models import Slider, Select


# In[2]:


df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2
                      )


# In[3]:


df_can.head()


# In[4]:


df_can.OdName.unique()


# In[5]:


# clean up the dataset to remove unnecessary columns (eg. REG) 
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

# let's rename the columns so that they make sense
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)

# for sake of consistency, let's also make all column labels of type string
df_can.columns = list(map(str, df_can.columns))

# set the country name as index - useful for quickly looking up countries using .loc method
df_can.set_index('Country', inplace=True)

# add total column
df_can['Total'] = df_can.sum(axis=1)

# years that we will be using in this lesson - useful for plotting later on
years = list(map(str, range(1980, 2014)))
print('data dimensions:', df_can.shape)


# In[6]:


df_can


# In[8]:


df_countries = df_can.loc[['Indonesia'],years].transpose()
df_total = pd.DataFrame(df_countries.sum(axis=1))
df_total.reset_index(inplace=True)
df_total.columns = ["Tahun", "Jumlah Imigran"]
df_total["Tahun"] = df_total["Tahun"].astype(int)

df_total


# In[16]:


a = figure(title='Jumlah Imigran Asal Indonesia yang Masuk ke Kanada Pada Tahun 1970-2013', x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)',
           plot_height=400, plot_width=700)


# In[17]:


a.line(x='Tahun', y='Jumlah Imigran', 
        color='red', legend_label='APPL Volume',
        source=df_total)

a.legend.location = 'top_left'


# In[22]:


curdoc().clear()
curdoc().add_root(row(a))

