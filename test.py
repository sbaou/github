import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

vix = web.DataReader("VIXCLS", "fred", "1941/1/1", "2018/05/16")
print(vix.head(1))
print(vix.tail(1))
