# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:37:56 2020

@author: stanleyhuang2
"""

import pandas as pd
import numpy as np

#Input excel filename below
df = pd.read_excel('appfindings2.xlsx', index=False)

#Import mapping file below (Group Name/Department Mapping)
df2 = pd.read_excel('mapping_data.xlsx')
df2.columns = ['Group Name', 'Practice']

