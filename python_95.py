import re
information='''
Mr. Saurabh Chorge
8998-8374-83
Address - Near Rnamla Hotel

Mr Adarsh Jadhav
9474.4747.85
Address - Near Bhuleswar Colony

Mrs Sahil Shinde
4574*4094*90
Address - Near Bhuleswar Colony

Mrs. Pranv Lala
4574&4094&90
Address - Near Bhuleswar Colony

Mr.Sushant Pawar
9457.2763.44
Address - Near Bhuleswar Colony

Mr Sushant Pawar
1212..2763.44
Address - Near Bhuleswar Colony

Sushant Pawar
400.2763.44
Address - Near Bhuleswar Colony

Sushant Pawar
500.2763.44
Address - Near Bhuleswar Colony
'''

# pattern = re.compile(r'\d\d\d\d.\d\d\d\d.\d\d')
# matches = pattern.finditer(information)
# for i in matches:
#     print(i)

# pattern = re.compile(r'\d\d\d\d[.-]\d\d\d\d[.-]\d\d')
# matches = pattern.finditer(information)
# for i in matches:
#     print(i)

# pattern = re.compile(r'[45]00[.-]\d\d\d\d[.-]\d\d')
# matches = pattern.finditer(information)
# for i in matches:
#     print(i)

# pattern = re.compile(r'[A-Z]\w\w\w\w\w\w\s[A-Z]\w\w\w\w\w')
# pattern2 = re.compile(r'[A-Z]\w\w\w\w\w\w')
# matches = pattern.finditer(information)
# matches2 = pattern2.finditer(information)
# for i in matches:
#     print(i)
# for j in matches2:
#     print(j)

# pattern = re.compile(r'Mr[s]?\.?\s[A-Z]\w+')
# matches = pattern.finditer(information)
# for i in matches:
#     print(i)

emails = '''
saurabhdc7575@gmail.com
sahilshide@gmail.com
wkdwqiugduweihf iuwe
dkehfuef @gmail.com
AdarshJadhav27@gmail.com
sushantpawar0707@university.edu
'''
pattern = re.compile(r'[a-zA-z]\w+[0-9]?@[a-zA-Z]\w+\.(com|edu)')
matches = pattern.finditer(emails)
for i in matches:
    print(i)