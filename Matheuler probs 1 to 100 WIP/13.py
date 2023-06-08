

L=[]#a list to store the 50 numbers
with open('q13inp','r') as f:
    l=f.readline()
    while l!='':
        L.append(int(l))#parsing the 50 digit numbers as integers
        l=f.readline()
#the above code runs without error so long as the q13inp file contains 100 lines of data which is 50 digit numbers only
SUM=0
for i in L:
    SUM+=i
SUM=str(SUM)
SUM10=SUM[0:10]#using string slicing to get the first 10 digits
print(SUM10)
