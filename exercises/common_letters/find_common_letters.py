# find out common letters between two strings 

def common_letters():
    str1=input("Enter first string: ")    
    str2=input("Enter seconde string: ")    
    # convert to set and remove duplicate letters
    s1=set(str1)
    s2=set(str2)
    print(s1)
    print(s2)
    # & operation extract common letters 
    common_list= s1 & s2 
    print(common_list)



common_letters()

