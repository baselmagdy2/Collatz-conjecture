def collatz(x):
    if int(x) % 2 == 0:
       print(int(x) // 2)
       return int(x) // 2
    else :
        print(int(x) * 3 +1)
        return int(x) * 3 +1
print("what number do you want to start the conjecture with? ")
x = int(input())
print("the results are:")
while x != 1 :
  x = collatz(x)
  
