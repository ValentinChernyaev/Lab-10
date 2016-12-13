#-------------------------------------------------------------------------------
# Name:        модуль24
# Purpose:
#
# Author:      Черняев Валентин
#
# Created:     13.12.2016
# Copyright:   (c) Черняев Валентин 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    return 0 if get_next.seed == 0 else (get_next.seed**2%100000 + 1)
get_next.seed = int(input())


i=0
ind=[]
min=1000000000
Number=get_next()

while Number!=0:

  if Number<min:
    min=Number
    ind=[]
   # print ("очищеный",ind)
    ind.append(i)
  elif Number==min:
    ind.append(i)

  Number=get_next()
  i+=1

print(' '.join([str(j) for j in ind]))