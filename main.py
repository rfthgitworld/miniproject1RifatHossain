# INF601 - Advanced Programming in Python
# Rifat Hossain
# Mini Project 1

# This project will be using the packages NumPy and Matplotlib in order to create 5 graphs that output as PNG files.
#
# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
# (10/10 points) Store this information in a list that you will convert to a array in NumPy.
# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this file with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.


import yfinance as yf
import pprint
import numpy as np
import matplotlib.pyplot as plt

myStocks = ['MSFT','AMZN','NVDA','QBTS','ORCL']
stockInfo = {}

for stock in myStocks:
    dat = yf.Ticker(stock)
    last10days = dat.history(period='10d')
    stockInfo[stock] = []
    for price in last10days['Close']:
        stockInfo[stock].append(price)
