"""

Remove all duplicates words from a given sentence

Sort words of sentence in ascending order

Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Hello" instead of the number and for the multiples of five print "Hi". For numbers which are multiples of both three and five print "Hi Hello".

Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a list

Write a program that accepts a sentence and calculate the number of letters and digits.

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Write a python program to convert alternate characters to capital letters
"""


s = "johnny johnny yes papa eating sugar no papa"
l = s.split()
k = []
print("program 1")
print("The entered string is",s)
print("After removing the duplicate: ")
for i in l:

	
	if (s.count(i)>=1 and (i not in k)):
		k.append(i)
print(" ".join(k))
print(" program 2 ")
l.sort()
print(l)
print(" program 3: ")
for i in range(1,50):
        word = "Hello" if not i % 3 else ""
        word = "Hi"+" "+word if not i % 5 else word
        word = str(i) if word == "" else word
        print(word)
print(" program 4: ")
list = []
for i in range(1000, 3001):
    arr = str(i)
    if (int(arr[0])%2==0) and (int(arr[1])%2==0) and (int(arr[2])%2==0) and (int(arr[3])%2==0):
        list.append(arr)
print(",".join(list))
print(" program 5: ")
str0 = input("Input a string: ")
d=l=0
for c in str0:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
print(" program 6: ")
u=l1=0
for c in str0:
    if c.isupper():
        u=u+1
    elif c.islower():
        l1=l1+1
    else:
        pass
print("uppercase: ", u)
print("lowercase: ", l1)
print(" program 7: ")
newstr=" "
strue=True
for i in str0:
    newstr += i.upper() if strue else i.lower()
    if i.isalpha():
        strue = not strue
print(newstr)
