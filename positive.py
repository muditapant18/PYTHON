n=int(input("enter the linmit:"))
list=[]
for i in range(n):
    element=int(input("enter the element:"))
    list.append(element)
print("element of list are:",list)
positive=0
for i in list:
    if i >= 0:
       print(i, end = " ")
