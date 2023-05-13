# F28PL Coursework 1, Python         <--- leave this line unchanged 

################################################################################
# Question 1   


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice versa. 
You may use the python methods real and imag without comment, but not complex -- use j directly instead.
"""
# ... to here

# Check: have you read the question?  Have you read the link above to see how complex number addition and multiplication work?   


# Your answer here


#####################################
# Question 1a


from re import L
from tkinter import Y
from pyparsing import java_style_comment
from functools import reduce


def cadd(c1, c2):
    #Sums the values in the first list
    a = c1[0] + c1[1]
    #Sums the values in the second list
    b = c2[0] + c2[1]
    return (a,b)


def cmult(c1,c2):
    '''
    Example:
    (3,2)(9,6) to be converted to (3+2j)(9+6j)
    (3+2j)(9+6j) => 27+18j+18j+12j^2
    Since i^2 = -1
    27+18j+18j-12
                15 + 36j
                |     |
               Real   Imaginary
    '''
    a = c1[0] #First real number
    b = c1[1]*1j #First complex number
    c = c2[0] #Second real number
    d = c2[1]*1j #Second complex number
    z = (a*c)+(a*d)+(b*c)+(b*d) #Replication of foil method to open brackets
                                # of (a + bj) (c + dj)

    return (z.real,z.imag) #Return the real and imaginary numbers


#####################################
# Question 1b

def tocomplex(x1, y1):
    # This method is used to convert a pair of integers to a complex number
    # Set first number to x1
    a = x1 
    # Converts and sets second number x2 to a complex number eg. 1j
    b = y1 * 1j 
    # Convert to x + yj format and return
    z = a + b

    return z


def fromcomplex(c):
    # This method converts from a complex type to a pair of integers
    #Takes the real number from the complex number c
     a = c.real
    #Takes the imaginary number from the complex number c
     b = c.imag
     #Puts the real and imaginary number into a paired tuple
     z = (a,b)
     return z

# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions 
* seqandi and 
* seqxori 
that implement pointwise AND (https://en.wikipedia.org/wiki/Logical_conjunction) and XOR (https://en.wikipedia.org/wiki/Exclusive_or) of boolean sequences.
For instance
 seqandi([True,True,False],[True,False,True])
should compute
 [True, False, False]
and
 seqxori([True,True,False],[True,False,True])
should compute
 [False, True, True]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqandr and seqxorr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqandlc and seqxorlc.
"""

#####################################
# Question 2a


def seqandi(l1, l2):
    # Creates a list names l3 to store the computed results
    l3 = []

    #For loop which iterates through the index of the list. Without range(len())
    # the loop would iterate through the elements of the list
    for i in range(len(l1)):
        #Compares if the boolean in index i of each of the lists are True, if yes then
        #adds true to the list l3 or else it adds false. There are 2 ways of doing this
        #either by using a logical operator "and" or a bitwise operator "&". I prefer using
        #and since its more convenient
        if l1[i] and l2[i] == True:
            l3.append(True)
        else:
            l3.append(False)
    return l3


def seqxori(l1, l2):
    # Creates a list names l3 to store the computed results
    l3 = []

    #For loop which iterates through the index of the list. Without range(len())
    # the loop would iterate through the elements of the list
    for i in range(len(l1)):
        #Compares if the boolean in index i of only one of the lists are True, if yes then
        #adds true to the list l3 or else it adds false. Since this question asks for
        #Exclusive or which is not possbile using logical operators, we will have to use
        #Bitwise operator "^" which will add true only if one of the elements are true
        if l1[i] ^ l2[i] == True:
            l3.append(True)
        else:
            l3.append(False)
    return l3


#####################################
# Question 2b


def seqandr(l1, l2):
    l3 = [] # List that will store the boolean after applying pointwise AND
    if len(l1) & len(l2) == 1: # Base case to check if the lists have only one boolean value.
        l3 = [l1[0] & l2[0]] # Comparison will return to l3, true value for the single boolean in the list only if both are true.
    else:
        #Else compares the first boolean values in the list then using recurssion repeat the process from index 1 till end
        l3 = [l1[0] and l2[0]] + seqandr(l1[1:],l2[1:])
    return l3

def seqxorr(l1, l2):
    l3 = [] # List that will store the boolean after applying pointwise XOR
    if len(l1) & len(l2) == 1: # Base case to check if the lists have only one boolean value.
        l3 = [l1[0]^l2[0]] # Comparison will return to l3, true value for the single boolean in the list only if one of them are true.
    else:
        #Else compares the first boolean values in the list then using recurssion repeat the process from index 1 till end
        l3 = [l1[0]^l2[0]] + seqxorr(l1[1:],l2[1:])
    return l3


#####################################
# Question 2c


def seqandlc(l1,l2):
    #Read this way:
    # Return true if element in same index of l1 and l2 is true, if not then 
    # return false, for all the values in l1
    l3 = [True if l1[i] and l2[i] == True else False for i in range(len(l1))]
    return l3

def seqxorlc(l1,l2):
    # Read this way:
    # Return true if only one of the elements in same index of l1 and l2 is true, if not then 
    # return false, for all the values in l1
    l3 = [True if l1[i] ^ l2[i] == True else False for i in range(len(l1))]
    return l3




# END ANSWER TO Question 2
################################################################################


###############################################################################
# Question 3


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
a. Mutable vs immutable types. Give at least two examples of each, with explanation.
b. Integer vs float types.
c. Assignment = vs equality == vs identity is.
d. The computational effects of a call to list on an element of range type, as in
 list(range(5**5**5)).
e. Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.

A.) Mutable types refers object types that can be changed or modified, for example lists and dictionaries where u can initialize a list or dictionary and add or delete elements later on.

Immutable on the other hand are objects that can't be changed or modified such as strings, integers or tuples, where you have to declare the varible/element during initializtion and won't be able to modify later on. Although there is a workaround to modify tuples, where you can convert the tuple to a list, change the values and convert back to a tuple. If you try to modify an immutables object such as a tuple the interpretor will raise an TypeError exception.

B.) Integers are whole numbers numbers without decimal values. For example x=6,y=10 are both examples of integers.

Floats are data types that store decimal or exponential values, for example floats can store values such as 2.4,1.1,3.1443435, 5e10 etc

C.) Assignment "=" is used to assign values to variable, for example name = "Faiz" will assign "Faiz" to a string called named.

    Equality "==" is used to check if variables have the same value, for example 
        if l1[0] and l2[0] == True:
            return True
        else: return false 
    
    will check if True exists in both 0th index of the lists and return True else it will return false

D.) list(range(5**5**5))
    Range() is a function that returns sequence of numbers from 0(default) to a specified number, for example Range(20) will create a sequence upto 20

    list() is a constructor which is used to create a list. In our scenario if we try to print or return range(5**5**5) it will return only the range with edge cases, using list will convert the sequence to a list.

    Now about the range of 5**5**5, this will return a very large sequence. Computing it into a list is not possbile by all computers due to hardware limitations. If the hardware is not capable and this function is run it will give an overflow error like this:
    " OverflowError: Python int too large to convert to C ssize_t "

E.) A slicing refers to breaking and returning certains values from a list, string etc. 
    Slicing is done by specifying the start and end index, for example a[3:6] will splice the list "a" and return values from index 3(inclusive) to 6(exclusive), meaning values in index 3,4,5 will be returned. There also exists negative slicing where the negative numbers start from the end of the list. For example in a list [0,1,2,3,4,5], a[-1] will return 5, similarly a[-5:-2] will return values 1,2,3.

    In list(range(10**10)[10:10]), a list of range 10 to the power 10, the [10:10] will splice from index 10 to index 10(not inclusive) hence returning an empty list.

    In list(range(10**10))[10:10], a list of values from 0 to 10^10 filtering the values from 10 to 10

"""



# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4

"""
Recall that `map(f, l)` applies a function pointwise to a list, so that 
   map(f, [x, y, z]) 
computes 
   [f(x), f(y), f(z)]
Call a *datum* something that is either an integer, or a list of data (datums).
Write a generalised mapping function `supermap` that applyies `f` pointwise to any integers inside a datum. 

So for example:
* supermap(f, -5) should return 'f(-5)'
* supermap(f, []) should return '[]'
* supermap(f, [5, [5]) should return '[f(5), [f(5)]]'. 

You may find it useful to consider `isinstance` or the following code fragment
   type(5) == int 

An answer that guts the question (e.g. by calling a supermap-like function in a Python library) may score no marks.
"""


def supermap(f, dat):
    datum = [] #List of integers
    for i in range(len(dat)): #For loop iterating through the number of items in the list
        if type(dat[i])==int: #Checks whether type of data in index i of dat is int
            datum.append(f(dat[i])) #Adds to list datum after applying function f to value in index i of dat
        elif type(dat[i])==list: #Checks whether type of data in index i of dat is a list
            datum.append(supermap(f,dat[i])) #Recursive part which if a list then repeats the previous process to the items of the list of list in dat before adding it to datum
        else:
            raise Exception("Only numbers and list of numbers accepted")
    
    return(datum)

# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5


"""
An encoding f of numbers in lists is as follows:
* f(0) = [] (0 maps to the empty list)
* f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.

This is an implementation of one possible encoding of the natural numbers in sets:
   https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
"""


def fenc(i):
    #Takes a number value and creates the number of lists in list set
    set = [] 
    if i == 0: 
        return set
    elif i!=0:
        setA = fenc(i-1)
        set = [setA,[setA]]
        return set


def fdec(l):
    # Takes the encoded lists and converts it to a number
    count = 0
    if l == []:
        return count
    else:
        while(l!=[]):
            count+=1
            l = l[0]
        return count


# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
Implement a generator `love` such that if we assign
 x = love()
then repeated calls to
 next(x)
return the strings 
 I love you 
 You love that I love you
 I love that you love that I love you
 You love that I love that you love that I love you
 I love that you love that I love that you love that I love you
 ...
For full marks, your answer should respect correct capitalisation, as above.

Note that this question is not asking you to program an endless loop that prints these values; your answer should be a generator that yields these values.
"""


def love():
    #Initialize list to store the statements
    array = ["I love you"]
    # Yield is a generator object which is being used as an iterator
    yield "".join(array)
    
    while True: 
        #Inserts "you love that" to the 0th index of array.
        array.insert(0, "you love that ")
        #capFirst seperates the first letter from the first element of the array and capitilizes it, after which it concatenates the rest of the letters.
        capFirst = "".join((array[0][0].upper()+array[0][1:])) + "".join(array[1:])
        yield capFirst
        # Insert i love that to the 0th index of array.
        array.insert(0, "I love that ")
        yield "".join(array)
        



# END ANSWER TO Question 6
################################################################################


#################################################################################
# Question 7

"""
Consider functions that remove all instances of an integer `i` from a list of integers `l`, implemented in three distinct ways:

1. `removeall_oo` repeatedly applies the list .remove method until there are no instances of `i` left (you may use other programming constructs, such as counting the number of integers in `l`, or using exception raisers and handles).  
2. `removeall_ft` uses `import functools` and `filter`.  
3. `removeall_rd` uses `import functools` and `reduce` (but not filter). 

So for example, 
   removeall_oo(0, [0, 0, 1])
should return
   [1]
and
   removeall_oo(0, [0, 0])
should return
   []
"""

def removeall_oo(i, l):
    #While function to go through all the values in l
    while i in l:
        #If else statement to check whether i exists in the list, if not the program will throw an exception
        if i in l:
            l.remove(i) #Remove i from list l
        else:
            raise Exception(i + " is not part of the list")
    return l

def removeall_ft(i, l):
    def func(x):
         #If else statement to check whether i exists in the list, if not the program will throw an exception
         #Using boolean logic to filter out i from the list l
        if i in l:
            if x == i:
                return False
            else:
                return True
        else:
            #Exception Handler
            raise Exception(i + " is not part of the list")

    a = list(filter(func,l))
    return a   

        
def removeall_rd(i, l):
    x = [] #List x to store the new values after i is removed
    #If else statement to check whether i exists in the list, if not the program will throw an exception
    if i in l:
        x = reduce(lambda a,b: a+[b] if b!=i else a+[],l,[])
    else:
        raise Exception(i + " is not part of the list")
    return x


# END ANSWER TO Question 7
################################################################################


##########################################################
# Question 8

"""
The *Sudan* function is documented here:
   https://en.wikipedia.org/wiki/Sudan_function
Implement the Sudan function as a Python function `sudan(n, x, y)` by orienting the equalities and making recursive calls as appropriate.

Be careful: even `sudan(2,2,2)` freezes up my machine.
"""

def sudan(n, x, y):
    total = 0 #Variable to store the final result
    if n==0:
        # f0 (x,y) will return the sum of x and y
        total = x+y
    elif y==0:
        #fn+1 (x,0) returns x
         total = x
    elif n!=0 and y!=0:
        # fn+1(x,y+1) will use recursion to return
        # Fn(Fn+1(x,y), Fn+1(x,y)+y+1)
        total = sudan(n-1,sudan(n,x,y-1),sudan(n,x,y-1)+y)
    return total
    


# END ANSWER TO Question 8
################################################################################



###############################################################################
# Question 9 

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""


"""
Here's a very brief example answer to Q11 above where "Python" is replaced by "Eggs".  Enjoy:

A chicken is cheap to keep, can produce an egg a day, and eggs come prepackaged and naturally resist spoilage.  For instance, eggs come out of a chicken with a natural antibacterial coating on their shells so that they can be stored at room temperature, which keeps transport costs low --- in the US eggs are washed, which stops them smelling of chickens' bottoms but removes this coating, which is why US eggs require refrigeration and UK eggs don't. 
[note now this combines *factual* and *technical* elements; an awareness of the egg as a thing, but also of supply chain economics, food safety, and a nice factoid which really proves I went beyond the first page of Google results -mjg] 

Eggs are nutritious, tasty, and filling.  They are easy to cook and are culturally well-established in the UK.  A proper superfood, in fact.  

Eggs do have dangers: when improperly handled they can carry salmonella.  More information at [hyperlink].  Eggs can crack, and then spoil quickly.  Occasionally eggs go invisibly bad, or the embryo incubates prematurely (nowadays, sophisticated scanning machines eliminate these from the food chain). 

Eggs also have applications in vaccine development, and unfortunately also in biological warfare as incubators for germs, and [more stuff here -mjg].

For the future, [stuff about vegans, changes in food preferences, vat-grown protein, environmental costs of keeping chickens, etc etc].

[I could keep this up for pages, I won't: we've gone beyond the shell of an answer, we've cracked it, and if we allow our enthusiasm to egg us on then it would over-egg the pudding and we'd get egg on our faces for writing a not-eggsactly-concise answer:  we stuffed enough eggs in this basket and should stop, before the reader finds it eggscrutiating.   
Now your turn please, with "Python" instead of "Egg".  Make me proud.  -mjg]
""" 
'''
Python is a very old but one of the most famous and widely used programming languages in this world. There are various areas python is used in the real world. For example, python is used to develop websites and webpages since it comes with a wide range of frameworks such as Flask, Django, Pyramid etc. and content management systems such as Django CMS and Wagtail. Python is also used to develop games, for example Battlefield 2 was a game developed in python using various libraries like Pygame, Pycap, PyOpenGL. Other popular games developed using python include Sims4 and World of tanks. Another major and trending use of python is in Machine learning and Artificial intelligence. Python’s security and stability allow huge machine learning models and intensive computations to run using libraries such as SciPy, Keras, Pandas, Tensorflow etc.

The reason why python is so popular is because it’s a very easy and simple to learn programming language. Python uses simple syntax and is open sourced which adds another reason to its fame. The language is also regularly updated and has a wide community. Considering all these points python is set to have a huge scope due to the increasing demand of AI, Data analytics

'''

# END ANSWER TO Question 9 
###############################################################################


###############################################################################
# Question 10

"""
a. Explain in words the difference between 
   ([],[],[]) 
and 
   [[]]*3.
b. Explain in words what x points to in memory after we execute the following two commands:
     x = []
     x.append(x)
"""
'''
A.)
([],[],[]) is a tuple with empty lists, as we mentioned in questions 3, tuples are immutable which means the values cant be changed easily. Any forced changes will result in memory location being changed

[[]]*3 on the other hand is a list and is easily changeble(mutable), any changes made to this list will not affect the memory locations.

B.)
    x = [] creates an empty list and x.append() adds new elements to that list. x.append(x) will try to add the list x to x, which means when calling this fucntion will return from the same memory location
'''
# END ANSWER TO Question 10 
###############################################################################

###############################################################################
# Question 11

"""
Python has infinite precision integer arithmetic.

Write your own infinite precision "sum", "product", and "to the power of" functions, that represent numbers as lists of digits between 0 and 9 with least significant digit first. 
Thus: 0 is represented as the empty list [], and 10 is represented as [0,1]. 
You may assume that numbers are non-negative (no need for negative numbers, or for subtraction).
Do NOT gut the question by mapping to python's native integers, performing the arithmetic there, and mapping back!
You may use earlier functions in the definitions of later ones. 

Add your own tests to the `test_cw.py` file.
"""

# map an integer n to its representation as a string of digits.
# no need to error-check for the case that n is negative
# e.g. iint(12) == [2,1]
def iint(n):
    l = [] #List to store the number as list
    if n>0:
        while n!=0:
            #takes the number n and extracts the ones, eg from 52 extracts 2
            ones = n%10
            #takes the number n and extracts the tens, eg from 52 extracts 5
            tens = int(n/10)
            #adds values to list l
            l.append(ones)
            n = tens
    return l

# map the string-of-digit representation back to integers
# e.g. pint(iint(12)) == 12 
def pint(I):
    #Converts from [2,1] to 12
    x = ""
    for i in I:
        x = str(i) + x
    return int(x)

# add two infinite integers
# e.g. iadd([5], [5]) = [0,1]
def iadd(I,J):
    x = (I[0]+J[0])
    return(iint(x))

# multiply two infinite integers
# e.g. imult([], [5]) = []
def imult(I,J):
    if (I==[] or J==[]):
        return []
    else:
        x = (I[0] * J[0])
        return(iint(x))
    

# raise I to the power of J
def ipow(I,J):
    x = (I[0]**J[0])
    return(iint(x))

# END ANSWER TO Question 11 
###############################################################################


###############################################################################
# Question 12

"""
Recall from Question 4 the notion of a *datum*.

a. Write a command `abstractsize` which inputs a datum and returns an integer measure of how much memory it occupies (cf. Question 10).
Note this measure should be in an abstract unit in which each integer occupies one unit of memory and each pair of square brackets occupies one unit of memory, modulo sharing, so that (for example) `[5,5]` has measure 3 --- one for the square brackets, and one for the two integer payloads.  (Do not try to return actual memory usage in bytes, since this will depend on implementation and on the size of the integer payload!) 
b. Write a command `compress` which inputs a datum, and outputs a datum that represents it and minimises abstract size.  Your code should be clear and well-commented with an explanation (if required) of the algorithm you use.

We're not looking for precise bytecounts and certainly not looking for speed or optimal performance.  Marks will be awarded for elegance, clear commenting, and understanding of the issues involved. 
"""
def abstractSize(Datum):
    #Stores final result to be returned
    count = 0 
    # isinstance is used to check if Datum is of type int
    if(isinstance(Datum,int)):
        count +=1 #Increment count
    else:
        #Increment count
        count += 1
        for i in range(len(Datum)): #For loop iterates through the values in Datum
            # isinstance is used to check if Datum is of type int
            if(isinstance(Datum, int)):
                #Increment count
                count +=1
            else:
                count += abstractSize(Datum[i])
    return count


def compressSize(Datum):
    # Checks type of Datum, if not int it returns an empty list, another way of checking can be done by isinstance as used in abstractSize
    if (type(Datum) != int):
        l = [] #List to store the compressed list
        for i in Datum: #Iterate through values in Datum
            if isinstance(i,list): #Checks if i is of type list
                l.extend(i) #Adds i to list l
            else: 
                l.append(i) #Adds i to list l
        return l 
    else:
        return Datum


# END ANSWER TO Question 12 
###############################################################################

###############################################################################
# Question 13 (bonus question) 

"""
The code below to define `equals23` takes up five lines and 83 characters, by my count. 
It is also ugly, redundant, and indirect.
Rewrite it, so that it is clean, compact, direct --- and takes up one line and 23 characters.
"""
# QUESTION 13
#Assigns x to 23 
equals23=lambda x:x==23
# END ANSWER TO Question 13 
###############################################################################
