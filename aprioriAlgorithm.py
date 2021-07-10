import numpy as np
import pandas as pd
import itertools as itertools

#minSup = int(input("Enter minimum support\n:- "))
minSup = 1

maxLen = 0

df = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
df.fillna(0, inplace=True)

#print (df)

transactions = []
for i in range(0,10):
    transactions.append([str(df.values[i,j]) for j in range(0,4) if str(df.values[i,j])!='0'])

#print (transactions)

count = len(transactions)

def uniqueCombinations(list_elements, comb):
    l = list(itertools.combinations(list_elements, comb))
    s = set(l)
    return list(s)

def uniqueInd(mainArr):
    comArr = []
    for i in mainArr:
        for j in i:
            if j not in comArr:
                comArr.append(j)
    return comArr

def checkMin(checkArr):
    items = set()
    dic = {}
    
    for item in checkArr:
        items.add(item)
        dic[item] = 1
        
        for transaction in transactions:
            #print (transaction)
            #transac.add(transaction)
            #print (transaction)
            transac = set(transaction)
            if transac.issuperset(items):
                dic[item] += 1
    
        if dic[item] < minSup:
            del dic[item]
            
    print (dic)
        #cnt = 0
        #items.clear()
        #transac.clear()
        
    #return checkArr               
    
for i in transactions:
    if len(i) > maxLen:
        maxLen = len(i)
        
oneComb = uniqueInd(transactions)
oneCombMin = checkMin(oneComb)
