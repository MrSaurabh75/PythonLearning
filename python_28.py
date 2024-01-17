# f-string --> 

# Normal way to add the varibles in a string
'''
address = ("Aditya Birla marg, Dattanager, {}, {}")
city = "Pune"
state = "Maharastra"
print(address.format(city,state))'''

# Using f-string 
name = "Saurabh Digambar Chorge"
city = "Pune"
state = "Maharastra"
address = (f"My name is {name} currently i am living at Rode Colony, Aditya Birla marg, Dattanager, {city}, {state}")
print(address)

# Printing float value using f-string
price = 49.09999
txt = f"The {price:.4f}"
print(txt)
