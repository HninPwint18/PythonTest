names=[]
while True:
    names.append(input('Enter Student name : '))
    other = input('Do you want to do again y/n?')
    if other == 'y':
        continue;
    elif other == 'n':
        break;
num =1
print('Student List')
for name in names:
    
    print(f'{num}. {name}')
    num+=1