#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      risha
#
# Created:     06-12-2025
# Copyright:   (c) risha 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(4))