#below application creates dataframe using pandas and write the content of that dataframe in xlsx file using excelwriter


import pandas as pd
from xlsxwriter import Workbook
data=[{'Name':'PPA','Duration':3,'Fees':1590},{'Name':'Python','Duration':3},{'Name':'PPA','Fees':1590}]
df=pd.DataFrame(data)
print(df)

writer=pd.ExcelWriter('MarvellousPandas.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1')
writer.save()