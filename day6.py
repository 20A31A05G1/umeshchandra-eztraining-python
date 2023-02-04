'''       #EXCEPTION HANDLING
a=100
b=0
try:
    print(a/b)
except Exception as e:
    print("please note number cant be divided by zero",e)
print("bye")'''


'''a=10
b=0
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("Dont give second number ",e)

finally:
    print("resource closed")'''

'''a=10
try:
    b=int(input("enter the number:"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note number cant be divided by zero",e)
except ValueError as e :
    print("Invalid input",e)
except Exception as e:
    print("other error",e)
finally:
    print("resource closed")'''


'''#raise keyword
x=105
if x%2!=0 :
    raise Exception('x should be even num')
else:
    print('x is even num...correct')'''

#prgrms
'''r=float(input('enter a num'))
area=3.14*r*r
print(area)'''

'''name=input("enter ur name:")
name1=input("enter ur name:")
print(name1,'',name)'''

'''class computer:   #class definition
    def config(self):  #config is a func
        print("yes")
lenova=computer()  #object1
lenova.config()
hp=computer()      #object2
hp.config()'''


'''#constructor
class employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID: %d \nName: %s" % (self.id,self.name))
emp1=employee("umesh",11)
emp2=employee("pavan",22)
emp1.display()
emp2.display()'''

'''#variables and var.acess in class and method
class computer():
    a=10
    b=20      #var in class
    print("class variable inside clas",a)
    def config(self):   #config is a func
        c=100           #var in method
        print("yes")
        print("instance access",self.b)   #accessing class var outside the method 
lenova=computer()  #obj1
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()    #obj2
print('dell',dell.a)
lenova.config()'''







































