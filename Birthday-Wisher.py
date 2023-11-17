key = ["nawaf", 'nora', 'mohammed', 'Ali']
value = [1,2,3,4]

def A(k, v) :
    dic = {}
    for n in range(0, len(k)) :
        key = k[n]
        value = v[n]
        dic[key] = value
    return dic
print(A(key, value))