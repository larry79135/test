import math
def isPrime(n): 
  if n <= 1: 
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
        
    if n % i == 0: 
        return "不是質數!!!!!"
  return "是質數!!!!!!111122334444"
p=isPrime(n)
print(p)  