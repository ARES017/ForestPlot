''' Example '''

# Importing libraries

import pandas as pd
import os

os.chdir('directory/')

# Importing Forest plot function

import Forestplot as flt

# Importing data required for plotting

model_estimate = pd.read_csv('directory/model_estimate.csv')
reported_estimate = pd.read_csv('directory/reported_estimate.csv')
text = pd.read_csv('directory/text.csv')

# Create Forest plot

flt.forestplot(model_estimate=model_estimate,text=text,clip=[0.2,7],xlab='x-values',colour=['r','g'],title='Example',grid=True,is_summary=True,reported_estimate=reported_estimate)
