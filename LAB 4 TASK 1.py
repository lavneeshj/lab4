

def nestd_sum(L):
   total = 0  
   for i in L:
       if isinstance(i, list): 
           total += nested_sum(i)
       else:
           total += i
   return total


def nes_sum(s):
   total1 = 0
   for x in s:
       if isinstance(x, list): 
           total1 += nes_sum(x)
       else:
           total1 += x
   return total1
print (nes_sum([1,2,3,[4,5,[12,33,6]]]) + nestd_sum([1,2,3,[4,5]]))






