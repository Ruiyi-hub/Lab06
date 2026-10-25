a=[1,2,3,4,5]
print([x for x in a if x!=3])
new_list=[]
for x in a:
    if x!=3:
        new_list.append(x)
print(new_list)