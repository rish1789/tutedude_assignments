#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rishabh
#
# Created:     07-12-2025
# Copyright:   (c) risha 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from io import UnsupportedOperation
try:
  '''# CREATING SAMPLE FILE
  fh = open("sample.txt","wt")
  fh.write("This is a sample file\nIt contains multiple line\n")
  fh.close()
  '''
  # READING FROM SAMPLE FILE
  fh = open("sample.txt",'rt')
  data = fh.readlines()
  for i, j in enumerate(data):
    print(f"Line {i+1}: {j}")
  fh.close()

except FileNotFoundError as file_Error :
  print(file_Error)

except UnsupportedOperation as Unsupported_Error:
  print(Unsupported_Error)
