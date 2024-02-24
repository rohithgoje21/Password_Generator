import random
letter=['a','b','c','d','e','A','B','C','D','E']
num=['1','2','3','4','5']
symbol=['(','<','^','!','_']

count_l=int(input('Enter no.of letters want to add : '))
count_n=int(input('Enter no.of digits want to add : '))
count_s=int(input('Enter no.of symbols want to add : '))

pw=[]
for i in range(1,count_l+1):
     char=random.choice(letter)
     pw+=char
for i in range(1,count_n+1):
     char=random.choice(num)
     pw+=char
for i in range(1,count_s+1):
     char=random.choice(symbol)
     pw+=char
# print(pw)

#imp..
password=random.shuffle(pw)

key=''
for i in pw:
     key+=i
print()
print("Password Generated is : ",key)
print()
