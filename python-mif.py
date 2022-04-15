import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

import plotly as pl 
import plotly.express as px

fhand=open('/Users/jpvasseur/py/MIF2.csv')
count=0
TotalDelay=0
TotalLoss=0

for line in fhand:
    count+=1
    fields=line.split(';')
    delay=fields[0]
    loss=fields[1]
    TotalDelay=TotalDelay+float(delay)
    TotalLoss=TotalLoss+float(loss)

print('Average loss:',TotalLoss/count)
print('Average delay:',TotalLoss/count)
print('number of records:',count)
