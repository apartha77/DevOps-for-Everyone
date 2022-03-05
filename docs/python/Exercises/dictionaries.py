# Example of dictionaries - if exists increment or add in dictionary
counts = dict()
names = ['test1', 'test2', 'test3', 'test2', 'test4',]
for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name]+1
print(counts)

#--------------------------------------
#Same operation in different way
