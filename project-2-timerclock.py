import time
def countdown(t):

    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)  #2 digits
        print(timer)
        time.sleep(1)
        t-=1
    print("FINISHED")

t=input('enter the time in seconds:')
countdown(int(t))
