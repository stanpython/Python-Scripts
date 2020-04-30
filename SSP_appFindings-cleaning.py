# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:32:39 2020

@author: stanleyhuang2
"""
import pandas as pd
import numpy as np
import datetime as dt
import tkinter as tk
from tkinter import filedialog


#import excel file (this will open a dialogue box asking user to select the excel file) Please ensure the data is in the first tab of the excel sheet
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 250, height = 275, bg = 'lightblue1')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path, sheet_name=0, index=False)
    root.destroy()

if __name__ == '__main__':
    browseButton_Excel = tk.Button(root, text='Click to select App Findings file (Selecting the wrong file will produce no result)', wraplength=80, command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(125, 125, window=browseButton_Excel)
    root.mainloop()
#Input excel filename below (Out of Scope)
    
#df = pd.read_excel('appfindings2.xlsx', index=False)

#Import mapping file below
df2 = pd.read_excel('mapping_data.xlsx', sheet_name='Sheet2')
#df2.columns = ['Group Name', 'Practice']

#delete blank rows
df = df.dropna(subset=['Pre - Production Application'])


#create practice column

df = pd.merge(df, df2, on='Group Name')


#define lookup parameters
def func(row):
    if row['Practice'] == 'BPG':
        return 'Hackermer, Thomas E'
    if row['Practice'] == 'Advisory':
        return 'Bell, Greg'
    if row['Practice'] == 'Tax':
        return 'Brown, Brad'
    if row['Practice'] == 'Audit':
        return 'Bishop, Matt'
    
df['CTO'] = df.apply(func, axis=1)


df.reset_index(drop=True, inplace=True)

#save file to specified file name
#writer = pd.ExcelWriter(dt.datetime.today().strftime("%Y%m%d") + '_app_findings-cleaned.xlsx', engine = 'openpyxl')

df.to_excel(dt.datetime.today().strftime("%Y%m%d") + '_app_findings-cleaned.xlsx', index=False)
