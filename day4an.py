'''printing squares using range
d={n:n*n for n in range(1,7)}
print(d)'''

'''#calculating product price for 5 units
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*2 for (product,price) in old.items()}
print(new)'''

'''#with checks
real={'sam':24,'rajesh':30,'umesh':11}
now={name:age for (name,age) in real.items()if(age>20)}
print(now)'''

'''#create a list with 8 customers names.Display a dictonary which has customer names along with discounts for them from a particular shop.
import random
cust=['a','b','c','d','e','f','g','h']
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)'''

'''#create two list,first list should have 5 students ,second list should have total marks for (1,500)
sname=['umesh','prem','david','rajesh','mahii']
smarks=[400,357,280,488,501]
stu_dict={sname:smarks for (sname,smarks)in zip (sname,smarks)}
stu_per={sname:(smarks*100)/500 for (sname,smarks) in stu_dict.items() if smarks<=500}
print(stu_per)'''

#strings
s="umesh"
print(s.lower())
print(s.upper())      
print(s.capitalize())
print(s.replace('h','a'))
print(s.strip())
print(s.split())
print(s.split(','))
print(s.split('.'))
print(s.count('e'))
print(s.find('e',0,len(s)))
print(s.index('e',2,len(s)))
print(s.islower())
print(s.isupper())
print(s.istitle())
print(min(s))



'''#get 1 string as input along with a character find out and display whether the character is present in string or not
s=input("string:")
c=input('chrt:')
if c in s :
    print("character is present")
else:
    print("character is not present")'''



'''#check whether the string is palindrome or not
s="mad"
s1=s[::-1]
k=1
for i,j in zip(s,s1):
    if i!=j:
        k=0
if k==1:
    print("Palindrome")
else:
    print("not")'''


''' #or
s="dadd"
if s[0:]==s[::-1]:
    print('yes')
else:
    print('no')'''


'''#check your string contains or not,if space are present then print the no of sapces in string
s=input("enter a string:")
cnt=0
for i in s:
    if i==" ":
        cnt=cnt+1
if cnt!=0:
    print(cnt)
else:
    print("no space")'''


'''#create a list with vowels get 1 string as input,count vowels from string
v=['a','e','i','o','u','A','E','I','O','U']
s=input("enter a string:")
count=0
for i in v:
    if i in s:
        count=count+1
print(count)'''     
    






























