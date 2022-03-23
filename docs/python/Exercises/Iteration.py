# Iteration - While - break - continue - for -  
# Definite Loop - While loop - run the loop for 5 times and then print hello world
# counter = 5
# while counter>0:
#     print("value is ", counter)
#     counter = counter-1
# print("Value of counter", counter)
# print("Hello World")
#-----------------------------------------------------------------
#Infinite Loop with break - unless you write "done" it will continue to run. You check the condition inside the loop, when number of iteration is not known
# while True:
#     line = input(">")
#     if(line=="done"):
#         break
#     print(line)
# print("Finally Done!")
#-----------------------------------------------------------------
# Infinite loop with "continue" and "break". Skip to next iteration without finishing the body of the Loop for current iteration.
# Print lines without # - if "#"" is encountered, it skips and if "done" then stops the loop
# while True:
#     line = input(">")
#     if (line[0]=='#'):
#         continue
#     if(line=="done"):
#         break
#     print(line)
# print("Finally Done!")
#-----------------------------------------------------------------
#Definite loop with for. Looping thru known set of items list, dictionaly, array,  
# letters = ["a","b","c","x","y","z"]
# for letter in letters:
#     print("current letter is", letter)
# print("Done!")
#-----------------------------------------------------------------
# To find the largest value in a list
largest = None
print('Before:', largest)
for itervar in [5, 41, 12, 3, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
#-----------------------------------------------------------------
