a = [1,2,3]
a += [4]
a.append(5)

a="hello"

print(a[:-1])

#simple dictionary
b = {}
b["value1"] = 4
b["value2"] = []
b["value2"]+= ["hello"]
b["value2"]+= ["bye"]

print(b)

#tuple
c = (1,2)
c = (1,2,3)
c = ((1,2),(3,4))
print(c)

#string tokenization
# d = "a,b,c,d,e"
# d = d.split(",")
# for i in d:
#     print(i)

def fun1(arg1, arg2):
    value = arg1 + arg2
    # return

# print(fun1(1,2))
# print(fun1([1,2],[3]))
# print(fun1("hello","world"))





# i = 0
# while i<len(a):
#     print(a[i])
#     i+=1

try:
    c = (1,2)
    c += (3)
except:
    print("You're an idiot")
