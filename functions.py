

def double_it(num):
 res = num *2
 return res

ans = double_it(10)
# print(ans)

#args
def allSum(*numbers):
 for num in numbers:
  print(num)
  
 return numbers
 
total = allSum(40,45,50) 
print(total)

def ful_name(first,last):
 name = f'Full name is: {first} {last}'
 return name
# take as perameter
# name=ful_name("Hello","Juii")
name=ful_name(last = "Juii", first="Hi")
print(name)
