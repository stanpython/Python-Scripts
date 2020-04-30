# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:44:09 2020

@author: stanleyhuang2
"""
import pandas as pd
import numpy as np
import datetime as dt
import tkinter as tk
from tkinter import filedialog


#import excel file (this will open a dialogue box asking user to select the excel file)
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 200, height = 200, bg = 'lightblue1')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path, sheet_name = 0, skiprows=1)
    root.destroy()

if __name__ == '__main__':
    browseButton_Excel = tk.Button(root, text='Click to select Data Collection file (Selecting the wrong file will result in error)', wraplength=80, command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(100, 100, window=browseButton_Excel)
    root.mainloop()

#df = pd.read_excel('Data Collection.xlsx', sheet_name='SSP1, SSP2, SSP4 (Data 1)', skiprows=1)

#De-Uppercase words in Column D (Business Group)
df['Business Group'] = df['Business Group'].str.rstrip()
df['Business Group'] = df['Business Group'].map({'TAX': 'Tax', 'BPG': 'BPG', 'Advisory': 'Advisory', 'Audit': 'Audit', 'Tax': 'Tax'})

#define lookup parameters
def func(row):
    if row['Business Group'] == 'BPG':
        return 'Hackermer, Thomas E'
    if row['Business Group'] == 'Advisory':
        return 'Bell, Greg'
    if row['Business Group'] == 'Tax': #or row['Business Group'] == 'TAX':
        return 'Brown, Brad'
    if row['Business Group'] == 'Audit':
        return 'Bishop, Matt'
    
df['CTO'] = df.apply(func, axis=1)

#Append "Hosted" to KPMG and Cloud

df['Hosting Location'] = df['Hosting Location'].map({'KPMG': 'KPMG Hosted', 'Cloud': 'Cloud Hosted', 'Vendor Owned/Hosted': 'Vendor Owned/Hosted'})

del df['S No']
#Create new excel spreadsheet
df.to_excel(dt.datetime.today().strftime("%Y%m%d") + '_data_collection-cleaned.xlsx', index=False)

