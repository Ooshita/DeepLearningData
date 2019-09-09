import sys
import numpy as np
import xlrd
import pandas as pd
import matplotlib.pyplot as plt

FILE = sys.argv[1]
book = xlrd.open_workbook(FILE)
s = book.sheet_by_name("Sheet1")

data_type = []
# 列分繰り返す
# excelのデータの型を読み込む
for i in range(s.row_len(0)):
    if s.cell_type(1,i) == 1:
        data_type.append(str)
    elif s.cell_type(1,i) == 2:
        data_type.append(int)

df = pd.read_excel(sys.argv[1],dtype={0:data_type[0], 1:data_type[1],2:data_type[2]})

print(df.dtypes)