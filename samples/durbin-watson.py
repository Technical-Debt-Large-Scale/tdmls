from statsmodels.regression.linear_model import OLS
import numpy as np
from statsmodels.stats.stattools import durbin_watson

def dw(data):
    ols_res = OLS(data, np.ones(len(data))).fit()
    return durbin_watson(ols_res.resid)

print("dw of range=%f" % dw(np.arange(2000)))
print("dw of rand=%f" % dw(np.random.randn(2000)))