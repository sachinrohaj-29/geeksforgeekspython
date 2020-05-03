import array

class SubArrayWithGivenSum:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tryingFunc(self):
        print("sachin rohaj", self.age)

abc = array.array('i', [1,2,3,4])
print(type(abc))

for i in range (0,2):
    print(abc[i])
ss = SubArrayWithGivenSum("sachin", 31)
ss.tryingFunc()