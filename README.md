# CPSC 458 Final Project

**Theme:** Portfolio recommendation given client preferences

**Members:** Tetsu Kurumisawa, Mina Bengi Aral


# Files

1. The original code (Jupyter Notebook, `final_project.ipynb`)
2. ReadMe file (`README.md`)
3. Initialization file (`initialization.py`)

# How To Run The Project

1) If running the initialization, go to `initialization.py`, assign the `OUTPUT_FILE` variable to your desired output file path and run it.
2) Then in the main jupyter notebook, change the Global Variables `INCOME_LIST`, `GROWTH_LIST`, `DEFAULT_LIST`, `ESG_LIST`, `INCOME_DICT`, `GROWTH_DICT`, `DEFAULT_LIST`, `ESG_DICT` to those stored in the `OUTPUT_FILE` generated in step 1.
3) If not running the initialization, run the main jupyter as it is. Change the parameters in the "USAGE EXAMPLES" section at the end to play around.

# Initialization

Running the `initialization.py` file runs the initialization. The initialization takes about an hour. To save time, we have pre-run this, and stored the outputs as global variables in the main jupyter notebook file. If you wish to run the initialization yourself, refer to the instructions in “How To Run The Project” section.

# Introduction

In our initial project proposal, we planned to create a program that determines the 5-day VaR for a given portfolio and recommend which stocks to swap if the risk was high. However, once we implemented the program to calculate the VaR for a given portfolio, we realized that we could use it for much more than that and decided to create a program that not only assesses the risk of a portfolio but recommends a portfolio to the user, given their portfolio type preference (default, income, growth, ESG), risk tolerance, which sectors to include, and the size of the portfolio.

# Implementation

## User input

The user specifies the desired portfolio type from income, growth, default, or ESG, risk tolerance in the form of 95% 5-day VaR (in ROI percentage), desired sectors to include, and the size of the portfolio.

## Recommendation process

### Portfolio types

Our approach was to classify stocks in S&P 500 into “income”, “growth”, “default”, and “ESG” categories. In doing so, we were able to pre-initialize our program and make it more efficient in replying to the client’s needs. This resulted in 4 lists of stocks with different strengths as well as the explanations for why they have such strengths. Stocks within each list are ordered from strongest to weakest in terms of how well they meet the expectations associated with each type of portfolio.

### Creating the list

In the initialization process, we rank each of the stocks in S&P 500 based on each type, income, growth, default (income & growth), and ESG. The evaluation is done by calculating the following parameters for each type.
- Income
	- Ranked based on their 
		- Beta
		- Principle protection
		- Projected dividend yield for the next 5 years
- Growth
	- Ranked based on their 
		- Forward P/E Ratio
		- Upside of the stock, calculated through a DCF Analysis of intrinsic value
		- Projection of the stock’s growth rate in the next 5 years, calculated by a linear regression on historical stock prices
- Default
	- A combination of income and growth parameters
- ESG
	- Within the best default stocks, ranked based on the ESG risk score

This ranking of stocks is done in the initialization.py file. Check the file for more details.

### Stock classification and selection

Once a client requests a portfolio, depending on the specified portfolio type, the program creates a copy of the respective list, which is named as the `working_list`. The reason we work with a copy of the list is to keep track of the stocks we have already picked from the list. Once a stock is picked, it is removed from the list so that if the need to pick another stock arises, the program can select the next best one.

The number of stocks selected from the list depends on the size determined by the client, as `small`, `medium`, and `large` sizes, which correspond to 4, 8, and 16 stocks, respectively. The choice of these special numbers (powers of 2) will be explained when clarifying the weight assignment procedure.

Sector information also plays a role in stock selection. Hence, when selecting stocks from the `working_list` for the formation of the initial `stocks_list`, a stock from each sector specified is selected. The rest is selected from the `working_list` starting from the top, i.e., the most suitable stock. Each stock included in the `stocks_list` is removed from the `working_list` since this list is used when picking another stock is required. In order to make this process more efficient, we assume that stocks already included in the `stock_list` do not exist in the `working_list`. Hence, leaving them in the `working_list` would result in duplicates.

### Weight assignment

A portfolio is defined as a dictionary of stocks with stock tickers as keys and their weights, i.e., percent presence in the portfolio as values. Hence, once the appropriate stocks that meet the client’s portfolio type requirements are met, the weights of each should be determined to obtain a complete portfolio. Several considerations determine this process.

One important consideration is the portfolio’s risk tolerance, which we determine via the Value at Risk (VaR) as RoI (returns on investment) percentage. In assigning the weights to each stock within the portfolio, we aimed to find the optimum combination of weights that would minimize the possible losses. This translates into seeking the set of percentages that would yield the highest VaR since the VaR indicates losses and is, hence negative. Our desire to minimize this negative value results in aiming to find the highest value.

To seek the combination with the highest VaR, we assumed a tournament approach. In our `scale(stocks, stock_dict, original_stock_list)` function, we take in a list of stocks and pick the first two items in the list. These two items are then passed into the `balance(group1, group2)` function. The workings of the balance function is outlined below, but essentially, it returns the optimal weights to be assigned to each item that would yield a high VaR.

Based on this return value, `scale` multiplies the weights that were already stored for each stock in the stock_dict by the weight determined by the balance function. Afterward, the two groups that were balanced are concatenated and inserted into the beginning of the `stock_list` as a list. The catch is this process is repeated until the length of the `stock_list` is reduced to one. What this effectively does in practice is pop and pick the two last items in the list. Then, the optimum weights for the two items are found and weights in `stock_dict` are updated accordingly. Then the next two items (the new last ones in the list) undergo the same process. Hence, starting with n number of elements in the list, i.e., individual stocks, the number of items are halved every time the algorithm goes through the whole list. Hence, if the individual stock number is n, the list length with pairs becomes `n/2`, and once the pairs are concatenated, it becomes `n/4` until `n/m`, where `m` is the number of stocks in each group, equals 1, i.e., `m=n` and there remains only 1 item in the `stock_list`, which is also comprised of a list of all the stocks. This progression is the reason portfolio sizes (number of stocks) are in powers of 2. At the final point, the algorithm has succeeded in ascribing weights to each stock. Once weights for all stocks are determined, the portfolio is returned as a dictionary of stocks and their respective weights.

<u>_An example progression can be seen below (a list of 4 elements):_</u>

	[(A), (B), (C), (D)] → Initial list
	[(C), (D), (A, B)] → After the first iteration
	[(A, B), (C, D)] → Second iteration; now each stock is paired up
	[(A, B, C, D)] → last iteration; now since the list includes one item, i.e., one list, the loop has come to an end

<u>_Another demonstration with a list of 8 elements_</u>

	[(A), (B), (C), (D), (E), (F), (G), (H)]
	[(A,B), (C,D), (E,F), (G,H)]
	[(A,B, C, D), (E, F, G, H)]
	[(A,B, C, D, E, F, G, H)]

### Picking the best portfolio

The `scale` function is called in the `create_portfolio_options(stocks, n)` function, in which `n` determines the number of different portfolio options wanted. This function is called by `best_portfolio`, which generates the options using the `create_portfolio_options` function and then chooses the best among them.

The `best_portoflio` function checks for two things: mean and VaR. If the mean is below 0 or the VaR value is not above the client's risk tolerance, the program looks for a way to improve the portfolio. This is called the swapping process, where the stock with the lowest weight is replaced by the next stock in the `working_list`. However, since sector preference is often important as a parameter indicated by the client, the selection of the stock to replace the former includes checking for its sector and making sure it has the same sector as the stock to be swapped. Once a stock deemed good for replacement is found, the whole process of determining the weights is repeated, making the `best_portfolio` function recursive, as once the swap occurs, this leaves us with a list of stocks that need weight assignments.

Here, another important consideration is that not all client requests are feasible, and sometimes cannot be accommodated. To detect this, our program has a counter for the number of attempts to find the `best_portfolio` and a `MAX_ATTEMPTS` limit, which we have determined as 3. Each time `best_portfolio` is called, it takes in the number of attempts so far and checks whether it has exceeded the limit. If the program is unable to find a suitable portfolio after three trials, we deem that the client’s preferences cannot be accommodated and recommend the client to change their preferences (e.g., increasing their risk tolerance).

The balance function takes in two lists (the number of items in the lists is unimportant) and aims to find weights that optimize their total VaR value. To do so, it resets the weight of each stock in the first group to 5 and those of the second group to 95 (over the length of each list for normalization purposes). Then the weights of each group are incremented (for the first group) and decremented (for the second group), and the resulting VaR value is stored. When each combination (in 5 percent discrete intervals) is tried, the list is sorted, and the weight combination with the highest VaR (least maximum loss possible) is selected as the appropriate balance, which is returned as two values.

## Program output

Once the program selects the best portfolio, it provides the following output:
- Stocks selected for the portfolio, along with,
	- Natural language explanations for reason of the selection of each stock
	- A graph to visualize the portfolio by representing each stock based on its percentage
- The weights of each stock, along with,
	- To further clarify the process to the client, we have included a graph that illustrates the VaR value for the portfolio

# References

https://www.investopedia.com/ask/answers/041615/what-riskmetrics-value-risk-var.asp
https://www.investopedia.com/terms/v/var.asp
https://www.investopedia.com/articles/04/092904.asp
