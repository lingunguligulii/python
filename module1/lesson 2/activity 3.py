import keyword

#Print a list of all keywords
print(keyword.kwlist)

#checking whether a particular word is a keyword
word = input("Enter the word: ")
print(keyword.iskeyword(word))