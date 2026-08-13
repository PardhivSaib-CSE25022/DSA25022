def rocketlaunch(n):

    if(n==0):
        print("Launch!")
        return

    print(n)

    return rocketlaunch(n-1)


#rocketlaunch(10)


def power(p, n):
   
    if n == 0:
        return 1
    
    
    return p * power(p, n - 1)

#print(power(2, 3)) 

def search(arr,target,k):

    if(arr[k]==target):
        return k

    if(k==0 and arr[k]!=target):
        return -1

    return search(arr,target,k-1)

arr = [2,54,7,4,6,0,365,-45]
#print(search(arr,10,len(arr)-1))

def fact(n):

    if(n==0):
        return 1

    return n*fact(n-1)

#print(fact(7))

def fib(n):

    if n==1:
        return 0

    if n==2:
        return 1

    return fib(n-1) + fib(n-2)

def fibseries(n):
    for i in range(1,n+1):
        print(fib(i))

    return "Done"

#print(fibseries(5))

 
    
      
    
    
