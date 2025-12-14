import pandas as pd
try:
  data=pd.read_csv('students.csv')
except exception:
  print('File not found.')
