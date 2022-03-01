#strname = input('What is your name?')
#print('Wecome',strname)
#-------------------------------------------------
#convert a Fahrenheit temperature to a Celsius temperature
#inp = input('Enter Fahrenheit Temperature: ')
#fahr = float(inp)
#cel = (fahr - 32.0) * 5.0 / 9.0
#print(cel)
#-------------------------------------------------
#width = 17
#height = 12.0
#print(width//2.0)
#intTest = 1 + 2 * 5
#print(intTest)
#type(intTest)
#strTest = '123'
#intTest1 = int(strTest)
#print(intTest1)
#-------------------------------------------------
# Test if and indentation
#x=2
#y=1
#if(x>y):
#   print('x is greater than y')
#-------------------------------------------------
#convert a Fahrenheit temperature to a Celsius temperature
#inp = input('Enter Fahrenheit Temperature:')
#try:
#    fahr = float(inp)
#    cel = (fahr - 32.0) * 5.0 / 9.0
#    print(cel)
#except:
#    print('Please enter a number')
#-------------------------------------------------
#Exercise : Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#intHours = input('Enter Hours:')
#Enter Rate: 10
#intRate = 10
#try:
#    intHour = int(intHours)
#except:
#    print('Enter hours in numbers')
#     quit()
#if(intHour>40):
#    intRate = intRate * 1.5
#    intPay = intHour * intRate
#    print('Since you have worked more than 40 hours you get', intPay)
#else:
#    intPay = intHour * intRate
#    print('Your pay is', intPay)

#-------------------------------------------------
#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6    F
strScore = input('Enter score between 0.0 and 1.0:')
try:
    floatScore = float(strScore)
    if(floatScore > 1):
        print('Please enter score within the range')
    elif(floatScore>=0.9):
        print('Grade achieved: A')
    elif(floatScore>=0.8):
        print('Grade achieved: B')
    elif(floatScore>=0.7):
        print('Grade achieved: C')
    elif(floatScore>=0.6):
        print('Grade achieved: D')
    elif(floatScore<0.6):
        print('Grade achieved: F')
except:
    print('Enter proper value')

#-------------------------------------------------



#-------------------------------------------------
