# More on String Methods
name = "saurabh Digambar Chorge !!!       "

# 1.Convert a string into UPPERCASE
print(name.upper())

# 2.Convert a string into lowercase
print(name.lower())

# 3.String Strip remove extra whitespaces
print(name.strip())

# 4.String rtrip removes trilling characters
print(name.rstrip("!"))

# 5.replace replaces the charachters in a string
print(name.replace("Saurabh","t"))

# 6.split converts a string into list
print(name.split(" "))
 
# 7.capitalizes the first charachter
str = "hello world"
print(str.capitalize())

# 8.centers the string 
print(name.center(50))

# 9.count counts the char how many time occurs in a string
print(name.count("a"))

# 10.The endswith method checks if the given string ends with a given value. If yes then returns True els returns False
print(name.endswith("!"))
print(name.endswith("e"))
print(name.endswith(" "))
print(name.endswith(" ",0,9))
print(name.endswith(" ",0,10))

# 11.find method searches a given value and returns a index if the value is not found returns -1
print(name.find("D"))
print(name.find("am"))
print(name.find("d"))

# 12.isalnum method checks your string has alphs numaric charchters
print(name.isalnum())

# 12.isalpha method checks your string has alphs charchters
print(name.isalpha())

# 13.islower checks is all char are lower case in a given string
print(name.islower())

# 14.isprintable if the all char are printable then returns true else returns false
print(name.isprintable())

# 15.isspace is there are white spaces in a string returns true
str1 = "       " 
print(str1.isspace())

# 16.istitle returns true only there is first char is capitalize in a string
print(name.istitle())