#-------------------------------------------------------------------------------
# Name:        модуль5
# Purpose:
#
# Author:      Черняев Валентин
#
# Created:     12.12.2016
# Copyright:   (c) Черняев Валентин 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def fact(f):
    c=[1,1]+(f-1)*[None]
    for i in range(2,f+1):
        c[i]=c[i-1]*i
    return(c[f])
def way(f,m):
    return int(fact(f+m)/(fact(f)*fact(m)))
c=list(map(int,input().split()))
print(way(c[0],c[1]))