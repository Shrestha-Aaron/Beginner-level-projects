import pandas as pd
try:
  data=pd.read_csv('students.csv')
except exception:
  print('File not found.')

#Result
def result(*subjects):
  percentage=sum(subjects)
  gpa=percentage/25
  return (percentage, gpa)

#Finds division, expects result in percentage
def DivisionFinder(x): 
  '''Expects result in percentage'''
  pass

