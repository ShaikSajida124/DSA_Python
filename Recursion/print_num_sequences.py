#Print n natural numbers
def printN(n):
  if n <= 0:
    return
  printN(n-1)
  print(n, end=" ")
print("Natural Numbers")
print("Ascending: ", end=" ")
printN(10)
print()

#print n natural numbers in reverse order
def printNReverse(n):
  if n <= 0:
    return
  print(n, end=" ")
  printNReverse(n-1)
print("Descending: ", end=" ")
printNReverse(10)
print()

#print n odd numbers starting from 1
def printOdd(n):
  if n <= 0:
    return
  printOdd(n-1)
  print(n*2-1, end=" ")
print("Odd Numbers")
print("Ascending: ", end=" ")
printOdd(10)
print()

#Print n odd numbers in reverse order
def printOddReverse(n):
  if n <= 0:
    return
  print(n*2-1, end=' ')
  printOddReverse(n-1)
print("descending: ", end=" ")
printOddReverse(10)
print()  

#Print n even numbers
def printEven(n):
  if n <= 0:
    return
  printEven(n-1)
  print(n*2, end=" ")
print("Even Numbers")
print("Ascending: ", end=" ")
printEven(10)
print()

#Print n even numbers in reverse order
def printEvenReverse(n):
  if n <= 0:
    return
  print(n*2, end=" ")
  printEvenReverse(n-1)
print("descending: ", end=" ")
printEvenReverse(10)
print()
