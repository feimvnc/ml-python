# dict is used to store key:value pairs 
def list_to_dict():
    keys = [1,2,3]
    values = ["a", "b", "c"]
    result=dict(zip(keys, values))
    print(result)

def l_to_d():
    k=[1,2,3]
    v=["a", "b", "c"]
    r=dict(zip(k,v))
    print(r)

#list_to_dict()
l_to_d()


# tuple is a collection of objects separated by comma
def dict_to_tuple():
    d={1: 'a', 2: 'b', 3: 'c'}
    for i in d.items():
        print(i)

dict_to_tuple()