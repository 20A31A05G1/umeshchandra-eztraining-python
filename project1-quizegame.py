q1='''what is the jersey number of MSDhoni?
a.11
b.7
c.27
d.3'''
q2='''which ipl team won the final in 2022?
a.chennai super kings
b.mumbai indians
c.royal challengers banglore
d.gujarat titans'''
q3='''how many times india won world cup(ODI)?
a.3
b.2
c.1
d.0'''
questions={q1:'b',q2:'d',q3:'b'}   #answers

name=input("Hi what is your name:")
print("Hello",name,"Welcome to the Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do u want to skip this que (yes/no)")
    if flag1=='yes':
        continue
    ans=input("enter your ans")
    if ans==questions[i]:
        print("Wow! you got one point")
        score=score+1
        print("your current score is :",score)
    else :
        print("wrong answer,u lost 1 mark")
        score=score-1
        print("ur current score is :",score)
    flag2=input("Do u want to quit? type (yes/no)")
    if flag2=='yes':
        break
print("Your total score is :",score)



    
                
