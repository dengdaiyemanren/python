# -*- coding: utf-8 -*-

__author__ = 'yinlg'  # Saeed Amen


from chartpy import Chart, Style, Canvas
import tushare.stock.trading as fd


# get your own free bQuandl API key from https://www.quandl.com/


# choose run_example = 0 for everything
# run_example = 1 - create a plain and Keen.io based template for a chart webpage

run_example = 0


if run_example == 1 or run_example == 0:

   
    df1 = fd.get_hist_data("300431",'2017-01-12')
    df1['code'] ="300431"
    df1['300431'] = df1['close']
    df2 = fd.get_hist_data("000786",'2016-03-12')
    df2['000786'] = df2['close']
     
    framses =[df1.filter(items=['300431']),df2.filter(items=['000786'])]
    #dfcontact = pd.concat(framses)
    dfcontact = df1.filter(items=['300431']).append(df2.filter(items=['000786']))
    

    chart_plotly1 = Chart(df=dfcontact, chart_type='line', engine='plotly',
                         style=Style(title="股价对比图", source="Quandl/Fred", scale_factor=-2, width=500, height=300, silent_display=True))


    text = "A demo of chartpy canvas!!"

    # using plain template
    canvas = Canvas([[chart_plotly1]])
    

    canvas.generate_canvas(silent_display=False, canvas_plotter='plain')
    
    
