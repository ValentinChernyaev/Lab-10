#-------------------------------------------------------------------------------
# Name:        модуль8
# Purpose:
#
# Author:      Черняев Валентин
#
# Created:     12.12.2016
# Copyright:   (c) Черняев Валентин 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

u=int(input())
def magic(u):
    mass=[1] + (u+1)*[0]
    for i in range(0,u):
        for j in range(i+1,u+1):
            mass[j]+= mass[j-i-1]
    print(mass[u])
magic(u)