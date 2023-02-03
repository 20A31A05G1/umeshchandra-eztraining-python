'''import random as r
x="good morning"
print(r.sample(x,5))

a=[1,2,3,4,5,6,7,8]
r.shuffle(a)
print(a)

a=[1,2,3,4,5,6,7,8]
print(r.choice(a))

b="welcome back"
print(r.choice(b))

a=r.random()
print(a)
#will return rand nnm b/w 0.0 to 1.0
#0.0 includes 1.0 excludes
print(r.randint(10,30))

a=[1,2,3,4,5,6,7,8]
print(r.choices(a,k=400))
#only k char

s="hello good day"
print(r.choices(s,k=5))

print(r.uniform(5,7))
#includes float values
#range values

#to find out all the functions in a module
z=dir(r)
print(z)


#display whole  year calendar
import calendar
print("full calendar")
print(calendar.calendar(2023))
print("paricular month")
print(calendar.month(2020,5))
print("set first day of the week")
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2022,12))

#prg-display date time
import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")   #lowercase
fv=a.strftime("%Y")   #uppercase
print("year short version",sv)
print("year full version",fv)'''



     #FUNCTIONS CONCEPT

'''#func without argu and without return value
def sample():  #def or des
    print("hi i'm umesh")
    print("welcome to class")
sample()  #call

print("today is a great day")
sample()

#func without argu and without return value
#multiplying numbers
def multi():
    x=int(input("enter a num"))
    y=int(input("enter a num"))
    z=int(input("enter a num"))
    prod=x*y*z
    print(prod)
multi()

#func without argu and with return value
def multi():
    x=int(input("enter a num"))
    y=int(input("enter a num"))
    z=int(input("enter a num"))
    prod=x*y*z
    return(prod)
res=multi()
print(res)

#func with argu and without return value
#static input
def multi(x,y,z):
    prod=x*y*z
    print(prod)
multi(3,4,5)

      #or 
#user input
def multi(x,y,z):
    prod=x*y*z
    print(prod)

x=int(input("enter a num"))
y=int(input("enter a num"))
z=int(input("enter a num"))
multi(x,y,z)
    
    
#func with argu and with return value
#static input
def multi(x,y,z):
    prod=x*y*z
    return (prod)
res=multi(3,4,5)
print(res)

      #or 
#user input
def multi(x,y,z):
    prod=x*y*z
    return(prod)

x=int(input("enter a num"))
y=int(input("enter a num"))
z=int(input("enter a num"))
res1=multi(x,y,z)
print(res1)'''


'''#lemons prgm using functions type 1
n=int(input("enter a number of lemons is in hand :"))
total=21
def excess():
    if n>total:
        a=n-total
        print(a)
excess()
def lower():
    if n<total:
        b=total-n
        print(b)
lower()    '''


'''#find factors of the given num using func type 1

def factors():
    for i in range(1,n+1):
      if n%i==0:
        print(i)
n=int(input("enter a number:"))
factors()



#print multiplication table using func type 3
def multi_table(n):
    for i in range(1,11):
        print(i,"X",n,"=",i*n)
n=int(input("enter a number :"))
multi_table(n)'''

'''#find out sum of digits of given numbers using func type 4
def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("enter a number:"))
res=digits(n)
print(res)'''


'''#recursive function
def display():
    n=int(input("enter a num"))
    if n==1:
        display()
    else:
        print("over")
display()'''

'''#factorial number
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)  #fun call-its call
result=fact(4)
print(result)
     #LOGIC
n=4
4*fact(3)
4*3*fact(2)
4*3*2*fact(1)
4*3*2*1*fact(0)
output is 24'''

'''#fibonacci series
n=int(input("enter a num:"))
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum,end=' ')
    count+=1
    a=b
    b=sum
    sum=a+b'''

'''#func returns more values
#add n sub of 2 numbers in one func
def add_sub(x,y):
    sub=x-y
    add=x+y
    return sub,add
res1,res2=add_sub(20,10)
print(res1)
print(res2)'''

'''#variable length method
def sum(*a):       #(*a)----variable length
    c=0
    for i in a:
        c=c+i
    print(c)
sum(2,3,4,5,6,6,6,)'''
    


































