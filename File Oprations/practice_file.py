with open('practice.txt','r') as f:
    data = f.read()
    if 'python' in data:
        print("Yes")
    else:
        print('No')