num1 = 0
Fiblist = []
num2 = 0
num3 = 1
#appends even fibonaccis numbers in list Fiblist
while num1 <= 4000000:
  num1 = num2 + num3
  if num1 % 2 == 0:
    Fiblist.append(int(num1))
  num2 = num3
  num3 = num1
print(Fiblist) #print the list
newtot = 0 
for i in Fiblist: #prints total of values in Fiblist
  newtot += i
print(newtot)