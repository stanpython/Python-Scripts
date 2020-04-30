# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:36:17 2020

@author: stanleyhuang2
"""

import pandas as pd
import numpy as np
import datetime as dt
import tkinter as tk
from tkinter import filedialog

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 200, height = 200, bg = 'lightblue1')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    root.destroy()

if __name__ == '__main__':
    browseButton_Excel = tk.Button(root, text='Click to select Data Collection (Cleaned) file', wraplength=80, command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(100, 100, window=browseButton_Excel)
    root.mainloop()


root2= tk.Tk()

canvas1 = tk.Canvas(root2, width = 200, height = 200, bg = 'lightblue1')
canvas1.pack()

def getExcel ():
    global df2
    
    import_file_path = filedialog.askopenfilename()
    df2 = pd.read_excel (import_file_path)
    root2.destroy()
    
browseButton_Excel = tk.Button(root2, text='Click to select Application Findings (Cleaned) file', wraplength=90, command=getExcel, bg='red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=browseButton_Excel)

root.mainloop()


#df = pd.read_excel('data_collection-cleaned.xlsx')
#df2 = pd.read_excel('app_findings-cleaned.xlsx')

str = ['No']
high = ['High']

#Create result sets for different columns needed for appendix

result = df[['PPA Record', 'Name of the Application', 'Business Group', 'Hosting Location', 'Last/Latest Test Date', 'Comments for delay/non compliance', 'In Compliance (Yes/No)', 'CTO']]

result2 = df2[['Finding ID', 'Helper - Project Name', 'Finding', 'Risk Rating', 'Practice', 'Open Date', 'Days Open', 'CTO', 'Response']]

result3 = df2[['Pre - Production Application', 'Finding ID', 'Helper - Project Name', 'Finding', 'Risk Rating', 'Group Name','Business Owner','Risk Acceptance Reasoning', 'Response', 'Open Date']]

#Filter the dataframes above

not_compliant = result[result['In Compliance (Yes/No)'].isin(str)]
high = result2[(result2['Risk Rating']=='High') & (result2['Response']=='Remediate Risk') & (result2['Helper - Project Name']!='KPMG Foundation')] 
med = result2[(result2['Risk Rating']=='Medium') & (result2['Response']=='Remediate Risk') & (result2['Helper - Project Name']!='KPMG Foundation')] 
acceptrisk = result3[(result3['Response']=='Accept Risk') & (result3['Helper - Project Name']!='KPMG Foundation')] 

#Sort each sheet 

high = high.sort_values(by='Days Open', ascending=False)
med = med.sort_values(by='Days Open', ascending=False)
acceptrisk = acceptrisk.sort_values('Risk Rating')


#Reset index column (A)
not_compliant.reset_index(inplace=True, drop=True)
not_compliant.index += 1

high.reset_index(inplace=True, drop=True)
high.index += 1

med.reset_index(inplace=True, drop=True)
med.index += 1

acceptrisk.reset_index(inplace=True, drop=True)
acceptrisk.index += 1

#Export to excel
writer = pd.ExcelWriter(dt.datetime.today().strftime("%Y%m%d") + '_appendix.xlsx', engine = 'openpyxl')

not_compliant.to_excel(writer, sheet_name = 'Not Compliant', index=True)
high.to_excel(writer, sheet_name = 'Very high & High')
med.to_excel(writer, sheet_name = 'Medium')
acceptrisk.to_excel(writer, sheet_name = 'Risk Accepted')

writer.save()
writer.close()