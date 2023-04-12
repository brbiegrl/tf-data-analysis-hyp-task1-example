import pandas as pd
import numpy as np


chat_id = 909631698 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
  count = np.array([x_success, y_success])
  nobs = np.array([x_cnt, y_cnt])
  value = 0.02
  stat, pval = proportions_ztest(count, nobs, value)
  if round(pval) == 1:
    return False
  return True
