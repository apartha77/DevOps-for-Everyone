## An Introduction to Python

We will learn Python from scratch. To learn any language we need to learn its elements, similar to what how we learn English. So let us see the elements of Python comparing it to English learning:
1. Vocalubary/words - variables and **Reserver words** - use this words the way Python expects us to use, we cannot use it as a **variable**. 
![Reserver Words](images/Python-ReserveWords.png)

2. Sentence structure - validate syntax patterns (set of instructions)
![Syntax](images/Python-SyntaxPattern.png)

3. Story structure - constructing a program for a purpose. Write 2-3 lines of script on command prompt >>>, interactive mode but not more, reason bigger set of scripts or instructions should be written in a file and save it with extension **.py** .py is python file. Thus choose ***Interactive*** vs ***Script*** as per your purpose. 

Control Flow
#### Expressions
- Constants - they don't change values assigned. 
- Reserve Words - as mentioned above, they have specific use, e.g., False, is, class, return, finally, none, if, for, lambda, try, break, in, etc.
- Variable - container which can contain values assinged. ```x= 1; y=2; z = x+y``` 
- Operator - ``` +, -, *, /``` are arithmetic operators
- Function - method to perform a task, takes input and can have output. 
- User Input - input() ``` name = input('who are you?')
print('Welcome', name)``` comma will add space inbetween
- Comments - ```# ```Python ignores lines starting with #.

#### Conditional Execution
- Comparisioin operators - ``` ==, >, >=, <, <=, != ``` Indenting is imporant here (4 spaces), depending upon indentation block of code will be executed, nesting will further indent the code. 
``` If (x==1):```  
```indent....print('indent applied')```
- Multi-way - if: and elif: and then else: (elif is new to me) one of the three will run. Multiple if can be written with elif, like if, then elif, then elif, then elif and finally may not may not have else. 
- The ``` try / except ``` structure (similar to try/catch). Surround code with try/except to handle errors. If code in try works then except is skipped, if code in try fails then except works. 
#### Functions
- Set of code store and reuse
![Function](images/Python-Function.png)
- Building Function - ```def MyFunction():``` this will hold my customer code. Now, invoke or call this function from wherever required. Function can take arguments(value) or parameters (variable), process them inside the function and return results. 
#### Loops - Repeated Steps    
- To create the loop we need Iteration, iteration variable to control the loop.
- Indifinite Loop -  Similar to ```If``` where condition is checked for a finite number of times before the loops ends. Example ```While, ```. We can create infinite loop and put a condition inside and then use ```break``` to stop the loop once condition is met and ```continue``` to send the control back to ```while```. Jumps to the "top" of the loop and starts the next iteration.
``` 
While True:
 line = input('>')
  if(line[0]==#):
   continue
  if (line =='done'):
   break
  print(line)
  ```

- Definite Loop - use ``` for in ``` for i in [5,4,3,2,1]: do...task 5 times. 

#### Python Data Structures

### String

### List

### Dictionary

### Tuple
- While manage disks and software package
- d
- d
``` 
#read file
fhandler1 = open("Test.txt")
dcount = dict()
for line in fhandler1:
    words= line.split()
    #create word dictionary - Idioms
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
#print the top 3 key & val
for val, key in lst[:3]:
    print(key,val)
```


#### Regular Expression
---
|Regular Expression | Meaning|
|---|---------------|
|^ | Matches the beginning of a line|
|$ | Matches the end of the line|
|. | Matches any character|
|\s|Matches whitespace|
|\S|Matches any non-whitespace character|
|*|Repeats a character zero or more times|
|*?|Repeats a character zero or more times (non-greedy)|
|+|Repeats a character one or more times|
|+?|Repeats a character one or more times (non-greedy)|
|[aeiou]|Matches a single character in the listed set|
|[^XYZ]|Matches a single character not in the listed set|
|[a-z0-9]|The set of characters can include a range|
|(|Indicates where string extraction is to start|
|)|Indicates where string extraction is to end|



#### Linux Common Commands - frequently used
##### Common Commands (part I)  
- cd to go straight to the home folder
- **cd-** (with a hyphen) to move to your previous directory
#### Common Commands (part II)
- cp – copy files
- mv – move or rename files

#### Common Commands (part II)

#### Common Commands (part II)

Reference:    
Check this ebook [Python](https://books.trinket.io/pfe/index.html)


---

[Next: Day 0](00-day00.md)

[Home](../index.md)

[Top](03-PythonIntro.md)



