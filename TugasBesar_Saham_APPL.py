#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Data handling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource


# In[2]:


#Read Data CSV
df_stock = pd.read_csv("Volume.csv")
print(df_stock.head())


# In[3]:


#Liat tipe data dari kolom Volume
df_stock['Date'] = pd.to_datetime(df_stock.Date)
print(df_stock.info())


# In[4]:


#Inisialisasi ke dataframe yang khusus menampung kolom volume
df_appl = df_stock['Volume']


# In[5]:


#Inisialisasi kedalam bentuk CDS agar dapat ditampilkan di figure
cds_appl = ColumnDataSource(df_stock)


# ## Pembuatan Figure
# 

# In[6]:


#Melakukan pembuatan figur dengan X-axis = Date dan Y-axis = Volume
fig = figure(x_axis_type='datetime',
                  plot_height=700,
                  plot_width= 1800,
                  x_axis_label='Date',
                  y_axis_label='Volume',
                  title='Volume')


# In[7]:


#Menentukan warna, dan source dari garis figur
fig.line(x='Date', y='Volume', 
        color='red', legend_label='APPL Volume',
        source=df_stock)

fig.legend.location = 'top_left'


# ## Pembuatan Hover
# 

# In[8]:


hov_appl = fig.circle(x='Date', y='Volume', source=cds_appl ,size=15, alpha=0, hover_fill_color='blue', hover_alpha=0.5)


# In[9]:


tooltips = [
            ('Date', '@Date{%F}'),
            ('Volume', '@Volume'),
           ]
fig.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}, renderers=[hov_appl]))


# In[10]:


show(fig)


# In[11]:


layout = row(plot)
curdoc().add_root(layout)

