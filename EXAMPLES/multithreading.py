#So multithreading is a way of running multiple things at once
#We can accomplish this by doing this

#1 - Without Join():
import threading
import time
def loiter():
    print('You are loitering!')
    time.sleep(5)
    print('You are not loitering anymore!')

t1 = threading.Thread(target = loiter)
t1.start()
print('Hey, I do not want to loiter!')

'''
Output without join()--> 
You are loitering!
Hey, I do not want to loiter!
You are not loitering anymore! #After 5 seconds --> This statement will be printed

'''
#2 - With Join():
import threading
import time
def loiter():
    print('You are loitering!')
    time.sleep(5)
    print('You are not loitering anymore!')

t1 = threading.Thread(target = loiter)
t1.start()
t1.join()
print('Hey, I do not want to loiter!')

'''
Output with join() -->
You are loitering!
You are not loitering anymore! #After 5 seconds --> This statement will be printed
Hey, I do not want to loiter! 

'''

#Credit: https://stackoverflow.com/questions/15085348/what-is-the-use-of-join-in-python-threading
# I'm too lazy to write out an example kekw