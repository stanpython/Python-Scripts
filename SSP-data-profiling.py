# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:11:21 2020

@author: stanleyhuang2
"""

import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport


df = pd.read_excel('app_findings-cleaned.xlsx')
df.profile_report(correlations={"cramers": {"calculate": False}})
profile = ProfileReport(df, title='Pandas Profiling Report')

profile.to_file(output_file="your_report.html")