# Parqet-Python

A simple package to interact with the Parqet API.

## Features
The parqet-python package will use the Parqet API to gather information about public Portfolios. Available infomration includes:
* Portfolio name
* Portfolio value
* Gain gross / net
* Total invested
* List of activities and holdings
* and many more..

## Getting Started

These instructions will tell you how to install the package and how to use it.

### Installing

Install the package via pip

    pip install parqet

### Usage
Create a `Portfolio` object and get the name of the portfolio:

    # This is an example of how to use the Portfolio class
    from parqet import Portfolio
   
    # Create a portfolio object
    portfolio = Portfolio("YOUR_PORTFOLIO_ID")
    
    # Print the name of the portfolio
    print(portfolio.get_name())