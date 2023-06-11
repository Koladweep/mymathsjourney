#oneline solution to finding sum of digits in 2^1000
print(sum([int(i) for i in list(str(2**1000))]))














#below is stepwise readable code(commented, but can be uncommented for testing):
'''
print(sum([int(i) for i in list(str(2**1000))]))
#the above code prints sum of digits (i's) in 2 ^1000
num=2**1000#number to find sum of digits for
#converting it into a string
digits=str(num)
#converting the numeric string into a list of individual strings representing digits
digits=list(digits)
#coberting string list to an integer list
digits=[int(i) for i in N]
#summing up using built in module sum(iterable item with integer values N)
s=sum(digits)
print(s)

'''














'''
#to make it reusable

#create a class of operations based on b'th exponential of a
class apowb:
    a=None
    b=None
    def __init__(self,a,b):
        if isinstance(a,int):
            self.a=int(a)
        else:
            raise ValueError("INVALID TYPE!  'a' can only be integer valued.")
        if isinstance(b,int):
            self.b=int(b)
        else:
            raise ValueError("INVALID TYPE!  'b' can only be integer valued.")

    def sumofdigits(self):
        return sum([int(i) for i in list(str(self.a**self.b))])
obj=apowb(2,'a')
print(obj.sumofdigits())
    
#or, for better readability with an added overhead of more variables and slightly longer execution time:
class apowb:
    a=None
    b=None
    def __init__(self,a,b):
        if isinstance(a,int):
            self.a=int(a)
        else:
            raise ValueError("INVALID TYPE!  'a' can only be integer valued.")
        if isinstance(b,int):
            self.b=int(b)
        else:
            raise ValueError("INVALID TYPE!  'b' can only be integer valued.")

    def sumofdigits(self):
        num=self.a**self.b
        #converting it into a string
        digits=str(num)
        #converting the numeric string into a list of individual strings representing digits
        digits=list(digits)
        #coberting string list to an integer list
        digits=[int(i) for i in N]
        #summing up using built in module sum(iterable item with integer values N)
        s=sum(digits)
        return s
obj=apowb(2,'a')
print(obj.sumofdigits())
