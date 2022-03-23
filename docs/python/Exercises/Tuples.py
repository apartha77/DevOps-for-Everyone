# Tuples - Examples
#---------------------------------------------------------------------
# 10-Mar-22 - Warm up
# print("hello world")
# filename = input("enter file name")
# if(len(filename)>0):
#     print(filename)
#-------------------------------------------------------------------
# 10-Mar-22 - Find larget in the collection 
# largest = None
# itemlst = list()
# itemlst= [3, 41, 12, 9, 74, 15]
# print('Before:', largest)
# for item in itemlst:
#     if largest is None or item > largest:
#         largest = item
#     print("Inside the loop", item, largest) 
# print("Finally the largest is", largest)
#------------------------------------------------------------------------
# 10-Mar-22 - Read a list, put in a Dictionary, Reverse the Dictionary
friends = ['Ravi', 'Gita', 'Sham']
# for friend in friends:
#     print('Happy New Year:', friend)
# print('Done!')
frienddic = dict()
frindlst = list()
newfrienddic = dict()
count=0
for friend in friends:
    frienddic[friend] = frienddic.get(friend,0)+1
    frindlst.append(friend)
    for key,value in frienddic.items():
        #newfrienddic = value,key
        newfrienddic[value, key] = newfrienddic.get(key,[key])
        count = count+1
    #newfrienddic = frienddic((v,k) for k,v in frienddic.items())
print("Total items:", count, newfrienddic)
#----------------------------------------------------------------------
