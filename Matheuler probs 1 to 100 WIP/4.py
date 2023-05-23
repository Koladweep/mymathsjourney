def palindrome(s):
  l = len(s)
  for i in range(l):
       if ( s[i] != s[l-i-1]):
          return False 
  #no inconsistency:
  return True
L=set()
found=False
for i in range(999,101,-1):
   for j in range(999,101,-1):
      prod=i*j
      if palindrome(str(prod)):
         L.add((prod,i,j))
print(max(L))