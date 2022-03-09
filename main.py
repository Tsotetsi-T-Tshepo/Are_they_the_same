#6 kyu Are they the "same"? https://www.codewars.com/kata/550498447451fbbd7600041c
print(comp(a1, a2))

def comp(array1, array2):
    if type(array2)==None:
        return False
    n=0
    for i in array1:
      n=i*i
      if n in array2:
          array2.pop(array2.index(n))
    return True if (len(array2)==0) else False
