import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 909631698 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    count = [x_success, y_success]
    nobs = [x_cnt, y_cnt]
    value = 0.02
    stat, pval = proportions_ztest(count, nobs, value)
    if pval >= value:
        return False
    return True
