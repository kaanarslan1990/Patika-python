t= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


def flat(t):
    flt_list = []
    for i in t:
        if isinstance(i, list) or isinstance(i, tuple):
            flt_list.extend(flat(i))
        else:
            flt_list.append(i)
    return flt_list

flat(t)
print(flat(t))
