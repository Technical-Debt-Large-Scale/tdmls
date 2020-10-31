# Process

## Hierarchical Regression Analysis

This section presents the process of performing multiple hierarchical regression analysis. It starts with the detection of unusual spots, and the unusual ones
stitches are removed after discussion between us.

We performed a linear regression in Scikit-Learn (https://scikit-learn.org). Linearity and independence are tested. Finally, report the results.

### A. Checking unusual points

There are three kinds of unusual points: outliers, high leverage points and highly influential points (chatterjee 1986). 

Dependent variable box plotting ![alt text][TD-Boxplot]

TD was created for identifying outliers. After the discussion, only one unusual point was removed from the dataset for a point on a website that did not add an analysis of the metric table data.

### B. Conduct hierarchical multiple

These data of each variable were inputted into Pandas (https://pandas.pydata.org) dataframe, statistics method was applied using Scipy (https://www.scipy.org) and Scikit-learn Linear Regression Model as the template formula, thus the regression model for this analysis is given as below:

y = B0 + B1X1 + B2X2 + B3X3 + B4X4

The independent variables were divided into four groups: 
    * group1: leadtime
    * group2: task complexity
    * group3: total developers
    * group4: task scaling

Each regression model is a combination of independent variables for a multiple regression.

The independent variable in the first group was inserted in the regression model. Then, a second multiple regression was performed with a new group of independent variables, together with the independent variables in the previous step. This process was repeated until all other independent variables were included in the regression model.

### C. Testing linearity

The partial regression plots are used to check the linear relationship between dependent variable and each independent variable (Fox 2015). Visually, from these regression plots in ![alt text][Regression], leadtime, task complexity, total developers and taskscaling shows a significant linear relationship with TD.

### D. Testing independence

It is assumed that observations between and within groups are independent. Independence of residuals was checked by analyzing Durbin-Watson statistics. If the value of Durbin-Watson test is between 1.5 and 2.5, there is no linear autocorrelation in the data (Ho 2013). The Durbin-Watson values in our tests are detailed in table below, which is acceptable. So, there is independence of residuals in our data.

| 	Feature 		   | value  | 
|-----------------|--------|
| leadTime			|	1.614	|
| complexityPoints| 	2.155	|
| totalDevelopers	| 	1.230	|
| taskScaling		| 	1.727	|

### E. Testing normality

The normal distribution of residuals is tested by visually checking the normal P-P plot (Ho 2013). In ![alt text][PPplot], the points on the plot remain close to the diagonal line, which means residuals are normally distributed. So, we do not violate the assumption of normality.

### F. Breusch-Pagan Test

You can see the following results for performing Breusch-Pagan Test in this case study: 

[('Lagrange multiplier statistic', 2.3261542987377517), ('p-value', 0.6760114026390507), ('f-value', 0.5291373984536129), ('f p-value', 0.7152904901671338)]

A Breusch-Pagan test uses the following null and alternative hypotheses:

The null hypothesis (H0): Homoscedasticity is present. 

The alternative hypothesis: (Ha): Homoscedasticity is not present (i.e. heteroscedasticity exists) In this dataset, the Lagrange multiplier statistic for the test is 2.326 and the corresponding p-value is 0.676. Because this p-value is not less than 0.05, we fail to reject the null hypothesis.

### G. Testing multicollinearity

We used VIF,Tolerance values to check multicollinearity (Alin 2010). The tolerance of independent variables should be greater than 0.1 for there to be no multicollinearity. In addition, the VIF should be less than 10. As you can see in Table below (VIF,Tolerance), the tolerance values in our study are all greater than 0.1 and the VIF values all less than 10. Therefore, there was no multicollinearity issue in this analysis.

| Model 	   | Lead Time 		| Task Complexity 	| Total Devs 	   | Task Scaling    |
|-----------|-----------------|--------------------|-----------------|-----------------|
| model1 	|    (1,1) 			| -              	   | -               | -               |
| model2 	|    (1.12, 0.89) | (1.12, 0.89) 		|  -              | -               |
| model3 	|    (1.60, 0.62) | (1.14, 0.88) 		| (1.57, 0.64) 	| -               |
| model4 	|    (1.76, 0.57) | (1.50, 0.67) 		| (1.82, 0.55) 	| (1.51, 0.66)    |

Chatterjee 1986 - Chatterjee Samprit, Hadi Ali S. Influential observations, high leverage points, and outliers in linear regression. Statistical Science. 1986;:379–393.

### H. Final regression model

Finally, the following regression model was presented as TD (y) and the following features LT (x1), TC (x2), DV (x3) and TS (x4). Thus, it was created the following formula  to represent the Multiple Regression Model:

y = 894.67 + 1.94x1 + 5.48x2 + 53.98x3 − 3298.65x4


Fox John. Applied regression analysis and generalized linear models. Sage Publications; 2015.

Ho Robert. Handbook of univariate and multivariate data analysis with IBM SPSS. Chapman and Hall/CRC; 2013.

Alin Aylin. Multicollinearity. Wiley Interdisciplinary Reviews: Computational Statistics. 2010;2(3):370–374.


[TD-Boxplot]: https://github.com/Technical-Debt-Large-Scale/tdmls/blob/master/pictures/TDM-Boxplot.png "TD Bloxplot"
[Regression]: https://github.com/Technical-Debt-Large-Scale/tdmls/blob/master/pictures/Regression.png "Regression partial plots of independent variables against TD"
[PPplot]: https://github.com/Technical-Debt-Large-Scale/tdmls/blob/master/pictures/PPplot.png
