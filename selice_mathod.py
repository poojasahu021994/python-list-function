    # 0    1    2     3   4    5    6     7   8   9   10
list=[12,  3,  44,'pooja',56,  7,  88,'sahu',33,  4,  5]
    # -11 -10 -9  -8      -7  -6  -5   -4    -3  -2  -1

print(list)
#list [start : end :jump]
# jump -->default 1
#end --> excluded (just before end)

a = list[3: 8: 1]
print(a)

b=list[3:8:2]
print(b)
