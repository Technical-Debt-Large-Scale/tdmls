# Process

## Hierarchical Regression Analysis

This section presents the process of performing multiple hierarchical regression analysis. It starts with the detection of unusual spots, and the unusual ones
stitches are removed after discussion between us.

We performed a linear regression in Scikit-Learn (https://scikit-learn.org). Linearity and independence are tested. Finally, report the results.

### A. Checking unusual points

There are three kinds of unusual points: outliers, high leverage points and highly influential points \cite{chatterjee1986influential}. 

Dependent variable box plotting ![alt text][TD-Boxplot]

TD was created for identifying outliers. After the discussion, only one unusual point was removed from the dataset for a point on a website that did not add an analysis of the metric table data.

### B. Conduct hierarchical multiple

These data of each variable were inputted into Pandas (https://pandas.pydata.org) dataframe, statistics method was applied using Scipy (https://www.scipy.org) and Scikit-learn Linear Regression Model as the template formula, thus the regression model for this analysis is given as below:

y = 0 + X1 + X2 + X3 + X4

The independent variables were divided into four groups: 

    * group1: leadtime
    * group2: task complexity
    * group3: total developers
    * group4: task scaling

Each regression model is a combination of independent variables for a multiple regression.

The independent variable in the first group was inserted in the regression model. Then, a second multiple regression was performed with a new group of independent variables, together with the independent variables in the previous step. This process was repeated until all other independent variables were included in the regression model.

### C. Testing linearity

The partial regression plots are used to check the linear relationship between dependent variable and each independent variable \cite{fox2015applied}. Visually, from these regression plots in Figure \ref{fig:RegressionPartialPlotsOfIndependentVariablesAgainstTechnicalDebt}, leadtime, task complexity, total developers and taskscaling shows a significant linear relationship with TD.

### D. Testing independence

It is assumed that observations between and within groups are independent. Independence of residuals was checked by analyzing Durbin-Watson statistics. If the value of Durbin-Watson test is between 1.5 and 2.5, there is no linear autocorrelation in the data \cite{ho2013handbook}. The Durbin-Watson values in our tests are detailed in   Table \ref{tab:durbin-watson}, which is acceptable. So, there is independence of residuals in our data.

### E. Testing normality

The normal distribution of residuals is tested by visually checking the normal P-P plot \cite{ho2013handbook}. In Figure \ref{fig:ppplotTechnicalDebt}, the points on the plot remain close to the diagonal line, which means residuals are normally distributed. So, we do not violate the assumption of normality.


### F. Testing multicollinearity

We used Tolerance/VIF values to check multicollinearity \cite{alin2010multicollinearity}. The tolerance of independent variables should be greater than 0.1 for there to be no multicollinearity. As you can see in Table~\ref{tab:multicollinearity-tolerance}. In addition, the VIF should be less than 10. As we can see in Table~\ref{tab:multicollinearity-vif}, the tolerance values in our study are all greater than 0.1 and the VIF values all less than 10. Therefore, there was no multicollinearity issue in this analysis.

[TD-Boxplot]: https://github.com/Technical-Debt-Large-Scale/tdmls/blob/master/pictures/TD-Boxplot.png "TD Bloxplot"
