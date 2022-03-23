# Example of dictionaries - if exists increment or add in dictionary
from unittest.util import _count_diff_hashable
#Process 1 - Lengthy process
counts = dict()
names = ['test1', 'test2', 'test3', 'test2', 'test4',]
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name]+1
#print(counts)
#--------------------------------------
#Same operation in different way using 'get' method of dictionary
newcounts = dict()
for name in names:
    # If new key then default by 0 and plus 1; if existing key then keyvalue +1; examples for histogram
    newcounts[name] = newcounts.get(name, 0)+1
#print('Revised method of get', newcounts)
#------------------------------------------
# Read a file and count the occurance of a word; print highest count
fhandler = open("Test.txt")
#print(fhandler)
try:
    lines = fhandler.read()
except:
    print("file does not exist")
    exit()
#print(lines)
words = lines.split()
#print(words)
counts = dict()
highestcount = 0
highestword=''
for word in words:
    counts[word] = counts.get(word, 0) + 1
    if (counts.get(word)>highestcount):
        highestcount = counts.get(word)
        highestword = word
    #print('highest count of word is:',highestcount)
    #print ('and the highest used word is:', highestword)
    #print(counts)
#----------------------------------------------------------
# Iterate thru the dictionary and print key and values
#for key in counts:
    #print("Key is", key, "and Value is", counts[key])
#print the keys
#print(counts.values())
#convert to list and print keys
# print(list(counts))
#print values
# #print(counts.values())
#-------------------------------------------------------------------------
# Two Iteration variables - same for loop to find highest count
bigcount = None
bigword = None
for k,v in counts.items():
    #print(k,v)
    if bigcount is None or v>bigcount:
        bigword = k
        bigcount = v    
#print(bigword, bigcount)
#--------------------------------------------------------------------------------
#read file - dictionary Idioms - use of Tuples - reverse the key value
fhandler1 = open("Test.txt")
dcount = dict()
for line in fhandler1:
    words= line.split()
    #create word dictionary - **Idioms**
    for word in words:
        dcount[word] = dcount.get(word,0)+1
#reversing the key & value order in the dictionary by the help of list and Tuple
lst = list()
for key, val in dcount.items():
    #new tuple in val, key order
    newtuple = (val, key)
    lst.append(newtuple)
#sort the list in reverse, big to small
lst = sorted(lst, reverse=True)
#print(lst)
# Now print the top 3 key & val
# for val, key in lst[:3]:
#     print(key,val)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#The same can be reduced to 
ffhander = open("Test.txt")
mcount = dict()
mlist = list()
for mline in ffhander:
    mwords = mline.split()
    for mword in mwords:
        mcount[mword] = mcount.get(mword,0)+1
# usling list comprehension - reduces the val, key reverse and sort at the sametime
mlist = sorted([(val,key)for key, val in mcount.items()], reverse=True)
#print top 3
print(mlist[:3])
#--------------------------------------------------------------
