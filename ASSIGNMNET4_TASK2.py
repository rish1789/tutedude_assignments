#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      risha
#
# Created:     07-12-2025
# Copyright:   (c) risha 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#WRITNG OPERATION OUTPUT.TXT FILE
text = input("Enter the text to write in the Output.txt file:")
with open("Output.txt",'wt') as fh:
  text += '\n'
  fh.write(text)
#APPENDING OPERATION
addition_txt = input ("Enter the additional text to append :")
with open("Output.txt",'at') as fh:
  fh.write(addition_txt)
#READING OPERATION
with open("Output.txt",'rt') as fh:
  print("Final Content of File:")
  print(fh.read())


