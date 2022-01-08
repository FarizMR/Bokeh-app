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
df_can = pd.read_csv('immigrant.csv')

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

df_countries = df_can.loc[['Indonesia'],years].transpose()
df_ind = pd.DataFrame(df_countries.sum(axis=1))
df_ind.reset_index(inplace=True)
df_ind.columns = ["Tahun", "Jumlah_Imigran"]
df_ind["Tahun"] = df_ind["Tahun"].astype(int)

source = ColumnDataSource(data={
    'Tahun'                : df_ind['Tahun'],
    'Jumlah_Imigran'       : df_ind['Jumlah_Imigran'],
})
#Melakukan pembuatan figur dengan X-axis = Date dan Y-axis = Volume
a = figure(title='Jumlah Imigran Asal Indonesia Yang Menetap di Kanada (1980-2013)',
                  plot_height=400,
                  plot_width= 700,
                  x_axis_label='Tahun',
                  y_axis_label='Jumlah Imigran')

#Menentukan warna, dan source dari garis figur
a.line(x='Tahun', y='Jumlah_Imigran', 
        color='blue', legend_label='Jumlah Imigran',
        source=source)

a.legend.location = 'top_left'

hov_appl = a.circle(x='Tahun', y='Jumlah_Imigran', source=source ,size=15, alpha=0, hover_fill_color='blue', hover_alpha=0.5)

tooltips = [
            ('Tahun', '@Tahun'),
            ('Jumlah Imigran', '@Jumlah_Imigran'),
           ]
a.add_tools(HoverTool(tooltips=tooltips, renderers=[hov_appl]))

curdoc().add_root(a)
