
<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/JoghurtConnaisseur/parqet-python/main/img/Parqet.png" alt="Parqet Logo" width="200">
  <img src="https://raw.githubusercontent.com/JoghurtConnaisseur/parqet-python/main/img/python.png" alt="Python Logo" width="200">
<br>
parqet-python
<br>
</h1>

<h4 align="center">An inoffical package to communicate with the <a href="https://www.parqet.com/" target="_blank">Parqet</a> API.</h4>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

## Key Features

The parqet-python package will use the <a href="https://www.parqet.com/" target="_blank">Parqet</a> API to gather information about public Portfolios. Available information includes:
* Portfolio name
* Portfolio value
* Gain gross / net
* Total invested
* List of activities and holdings
* and many more...

## How To Use

### Installation

Install the package via pip. This will also install the dependency loguru for logging purposes.

```bash
# Install the package
$ pip install parqet
```

### Usage
Create a `Portfolio` object and get the name of the portfolio.

```python
# Import the package
from parqet import portfolio

# Create a portfolio object
portfolio = Portfolio("YOUR_PORTFOLIO_ID")

# Extract the portfolio name and print it
print(portfolio.get_name())
```


> **Note**
> Your portfolio has to be set to public to access it via the API.

<details>
    <summary>Full list of functions</summary>
    <table>
  <thead>
    <tr>
      <th>Function Name</th>
      <th>Description</th>
      <th>Return Type</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>get_name()</td>
      <td>Returns the name of the portfolio.</td>
      <td><code>str</code></td>
      <td><code>portfolio.get_name()</code> returns <code>"My Portfolio"</code></td>
    </tr>
    <tr>
      <td>get_value()</td>
      <td>Returns the current value of the portfolio.</td>
      <td><code>float</code></td>
      <td><code>portfolio.get_value()</code> returns <code>6000.0</code></td>
    </tr>
    <tr>
      <td>get_total_gain_gross()</td>
      <td>Returns the total gross gain of the portfolio.</td>
      <td><code>float</code></td>
      <td><code>portfolio.get_total_gain_gross()</code> returns <code>1000.0</code></td>
    </tr>
    <tr>
      <td>get_total_invested()</td>
      <td>Returns the total amount invested in the portfolio.</td>
      <td><code>float</code></td>
      <td><code>portfolio.get_total_invested()</code> returns <code>5000.0</code></td>
    </tr>
    <tr>
      <td>get_total_gain_net()</td>
      <td>Returns the total net gain of the portfolio.</td>
      <td><code>float</code></td>
      <td><code>portfolio.get_total_gain_net()</code> returns <code>800.0</code></td>
    </tr>
    <tr>
      <td>get_total_return_gross()</td>
      <td>Returns the total gross return of the portfolio.</td>
      <td><code>float</code></td>
      <td><code>portfolio.get_total_return_gross()</code> returns <code>20.0</code></td>
    </tr>
    <tr>
      <td>get_total_return_net()</td>
      <td>Returns the total net return of the portfolio.</td>
      <td><code>float</code></td>
      <td><code>portfolio.get_total_return_net()</code> returns <code>16.0</code></td>
    </tr>
    <tr>
      <td>get_fees()</td>
      <td>Returns the total fees paid for the portfolio.</td>
      <td><code>float</code></td>
      <td><code>portfolio.get_fees()</code> returns <code>50.0</code></td>
    </tr>
    <tr>
      <td>get_created_at()</td>
      <td>Returns the date of the portfolio's creation.</td>
      <td><code>str</code></td>
      <td><code>portfolio.get_created_at()</code> returns <code>"2023-05-25T20:45:04.802Z"</code></td>
    </tr>
    <tr>
      <td>get_holdings()</td>
      <td>Returns a list of holdings in the portfolio.</td>
      <td><code>list</code></td>
      <td><code>portfolio.get_holdings()</code> returns <code>[{...}]</code></td>
    </tr>
    <tr>
      <td>get_activities()</td>
      <td>Returns a list of activities of the holdings in the portfolio.</td>
      <td><code>list</code></td>
      <td><code>portfolio.get_activities()</code> returns <code>[{...}]</code></td>
    </tr>
  </tbody>
</table>
</details>

## Download

If you don't want to install the package via pip, you can instead [download](https://github.com/JoghurtConnaisseur/parqet-python/releases/latest) the latest release of the sourcecode.

## Credits

This software uses [Loguru](https://github.com/Delgan/loguru) for logging. 

## License

GPL

---

> GitHub [@JoghurtConnaisseur](https://github.com/JoghurtConnaisseur) &nbsp;&middot;&nbsp;

