text1 = "python"
text2 = "programming"

#Length of the string
print(len(text1))

#Uppercase
print(text1.upper())

#Lowercase
print(text1.lower())

#Slicing
print(text1[0:3]) #text1[start_index : end_index+1]

#Reverse
print(text1[::-1])

#Find
print(text1.find('t'))

#Concatenate
text3 =  text1 + " " + text2
print (text3)