def linear_combination(*datas):
    get_size_first = len(datas[0])
    
    new_vector = [0 for _ in range(get_size_first)] 
    
    for data in range(len(datas)):
        if len(datas[data]) != get_size_first:
            raise ValueError("invalid size")
        for elem in range(len(datas[data])):
            new_vector[elem]+=datas[data][elem]
    
    return new_vector
            

def dot_product(*datas):
    get_size_first = len(datas[0])
    test = [1 for _ in range(get_size_first)] 
    for data in range(len(datas)):
        if len(datas[data]) != get_size_first:
            raise ValueError("invalid size")
        for elem in range(len(datas[data])):
            test[elem] *= datas[data][elem]
    
    return sum(test)
            
            

data1 = [1,2]
data2 = [4,5]

print(dot_product(data1, data2))