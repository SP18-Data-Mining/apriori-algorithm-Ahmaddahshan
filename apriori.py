# Ahmad Dahshan
# Data Mining
# Apriori Algorithm

transData = [ ['a','c','e'], ['b','c','e'],['a','b','c','e'], ['b','e','d'] ]

# This holds the itemsets that frequently occur in the database
frequencyList = [ ]
# A candidate list - the cardinality of Fk with each element in the database
candidateList = []

# Find the longest set in the database
maxSetLen = 0
for currentSet in transData:
	if (len(currentSet) > maxSetLen):
		maxSetLen = len(currentSet)

# frequencyList =  [maxSetLength] where all the sets are empty
for index in range(maxSetLen):
	frequencyList.append(set())


# generate C(1)-- candidateList1  and F(1) frequencyList
candidateMap = {}
for currentSet in transData :
	for element in currentSet :
		if element in  candidateMap.keys(): #print element set
			candidateMap[element] = candidateMap[element] + 1
		else:
			candidateMap[element] = 1


removeList = []
# Removing all the frequency of 1 from candidateMap
f1 = { i:candidateMap[i]  
    for i in candidateMap 
        if candidateMap[i] != 1 
    
}

#  frequentList[0] are the single frequent items
frequencyList.append(f1)  
removeList.append(  { i:candidateMap[i]  
    for i in candidateMap 
        if candidateMap[i] == 1 
    
} )

def checkDuplicates(check, result):
             duplicateSet = False
             for element in check:
                   if element == result:
                        duplicateSet = True
             if duplicateSet == False:
                   check.append(result)
                   
def multiplySet(trand,kset,k):
              
           ckplus1=[]
           for elementData in trand:
                            for iset in kset:
                                    result=list(set().union(iset,elementData))
                                    if len(result)== k+1:
                                         checkDuplicates(ckplus1,result)
           return ckplus1 
           
k=2
k_1Set = f1.keys()
while (frequencyList[k] != 0):	
	check=multiplySet(transData,k_1Set,k) 
	
	k += 1
	
	if  k == len(frequencyList[k]):
	    break
	# Output
	print check
