input = [[1, 2], [3, 4], [5, 6, 7]]
res = []

def reverse(x):
    x.reverse()
    for i in x:
        if isinstance(i,list) or isinstance(i, tuple):
            i.reverse()
            res.append(i)
reverse(input)
print(res)