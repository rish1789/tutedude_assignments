#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      risha
#
# Created:     09-12-2025
# Copyright:   (c) risha 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
students_details = {}
names = list(input("Enter the Student Name ").split())
marks = list(map(int,input("Enter the Student Marks ").split()))

for i in range(len(names)):
  students_details[names[i]]=marks[i]

nm = input("Enter the Name :")
if nm not in students_details:
  print("Student Not Found")
else:
  print(f"{nm}'s marks : {students_details[nm]}")