from datetime import datetime
import time


# Part 1
def clock(n):
    # Your code here
    """
        outputs time in hours minutes and seconds, every second for n seconds
        
        Parameters
        ----------
        n: int
            the number times that the seconds is to be incremented

        Returns
        --------
        None
    """
    for i in range(n):
        poop = str(datetime.now())
        poop = poop[11:19]
        print(poop,end="\r")
        time.sleep(1)


# Part 2
def lcm(a, b):
    """
        description --> returns the lowest common multiple of 2 numbers
        parameters --> a and b are numbers
        output --> lcm'
        examples--> lcm(8,10) --> 40
    """
    # Your code here
    a1,b1 = a,b
    while(a1!=b1):
        if a1>b1:
            b1+=b
        else:
            a1+=a
    return a1


# Part 3
def gcf(a, b):
    """
        description --> returns the greatest common factor of 2 numbers
        parameters --> the 2 numbers
        output --> the greatest common factor
        examples --> gcf(8,10) --> 2
    """
    # Your code here
    a1,b1=a,b
    while (b1!=0):
        b1,a1 = a1%b1,b1
    return a1