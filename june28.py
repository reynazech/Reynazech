"""
1.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
2.	Split a given string on hyphens into several substrings and display each substring

3.	Remove all the characters other than integers from string

4.	Add item 70 after 60 in the following Python List
list1 = [10, 20, [30, 40, [50, 60], 50], 30, 40]   
5.	Given a Python list, find value 20 in the list, and if it is present, replace the first occurrence of it with 200
"""
print("program 1")
count = 0
words=['ada', 'ann', 'pqr', '1331']
print("words=['ada', 'ann', 'pqr', '1331']")
for word in words:
    if len(word) > 1 and word[0] == word[-1]:
        count += 1
print("The count is: ",count)

print("program 2")
str = "let's-go-for-a-party"
print("The String is:", str)
substr = str.split("-")

print("Displaying each substring")
for sstr in substr:
    print(sstr)
print("Program 3")
strnum= "r1e2y3n4a5"
print ("the string : ", strnum)
integers = list([val for val in strnum
			if val.isnumeric()])
result = "".join(integers)
print ("final string", result)
print("Program 4")
list1 = [10, 20, [30, 40, [50, 60], 50], 30, 40]   
list1[2][2].append(70)
print(list1)
print("Program5")
index = list1.index(20)
list1[index] = 200
print(list1)
