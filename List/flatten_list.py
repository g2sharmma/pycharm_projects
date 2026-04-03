"""Method 1"""

def flatten(l):
    for item in l:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


lst = [1, 2, [3, 4, [5, 6], 7], 8]
x = list(flatten(lst))
print(x)

# for x in flatten(lst):
#     print(x)


"""Method 2 using Generator"""

def flat(lst):
    res = []
    for item in lst:
        if isinstance(item, list):
            res.extend(flat(item))
        else:
            res.append(item)
    return res

l = [1, 2, [3, 4, [5, 6], 7], 8]
print(flat(l))