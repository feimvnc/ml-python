from operator import index


str=input("enter a str: ")
li=str.split()
l=0
for i in li:
    count=li.count(i)
    print(f"{i}-{count}")
    #if(li.index(i)==len(li)):
        #print(f"{i}-{count}")
    