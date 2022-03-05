# Example of dictionaries - if exists increment or add in dictionary
from unittest.util import _count_diff_hashable


counts = dict()
names = ['test1', 'test2', 'test3', 'test2', 'test4',]
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name]+1
#print(counts)

#--------------------------------------
#Same operation in different way using get method of dictionary
newcounts = dict()
for name in names:
    # If new key then default by 0 and plus 1; if existing key then keyvalue +1; examples for histogram
    newcounts[name] = newcounts.get(name, 0)+1
#print('Revised method of get')
#print(newcounts)
#------------------------------------------
# Read a file and count the occurance of a word; print highest count
fhandler = open("Test.txt")
#print(fhandler)
lines = fhandler.read()
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
print('highest count is:',highestcount)
print ('highest used word is:', highestword)
#print(counts)











