n = int(input ("enter the limit "))  
n1 = 0  
n2 = 1  
count = 0  
if n <= 0: 
    print("invalid")
elif n == 1:  
    print ("The Fibonacci series of the numbers", n, ": ")  
    print(n1)  
else:  
    print ("The fibonacci series of the numbers is:")  
    while count < n:  
        print(n1)  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count += 1  
