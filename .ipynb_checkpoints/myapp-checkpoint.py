# Data handling
import pandas as pd
import numpy as np

# Bokeh libraries
from bokeh.io import output_file, output_notebook,curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.plotting import figure

#Read Data CSV
df_stock = pd.read_csv("./data/Volume.csv")
print(df_stock.head())

#Liat tipe data dari kolom Volume
df_stock['Date'] = pd.to_datetime(df_stock.Date)
print(df_stock.info())

#Inisialisasi ke dataframe yang khusus menampung kolom volume
df_appl = df_stock['Volume']

#Inisialisasi kedalam bentuk CDS agar dapat ditampilkan di figure
cds_appl = ColumnDataSource(df_stock)

#Melakukan pembuatan figur dengan X-axis = Date dan Y-axis = Volume
fig = figure(x_axis_type='datetime',
                  plot_height=700,
                  plot_width= 1800,
                  x_axis_label='Date',
                  y_axis_label='Volume',
                  title='Volume')

#Menentukan warna, dan source dari garis figur
fig.line(x='Date', y='Volume', 
        color='red', legend_label='APPL Volume',
        source=df_stock)

fig.legend.location = 'top_left'

hov_appl = fig.circle(x='Date', y='Volume', source=cds_appl ,size=15, alpha=0, hover_fill_color='blue', hover_alpha=0.5)

tooltips = [
            ('Date', '@Date{%F}'),
            ('Volume', '@Volume'),
           ]
fig.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}, renderers=[hov_appl]))

curdoc().add_root(fig)
