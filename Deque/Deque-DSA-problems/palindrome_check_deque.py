#import Deque Class
def is_palindrome(string):
  container = Deque()
  for char in string:
    container.insert_at_rear(char)

  while len(container) > 1:
    if container.get_front() == container.get_rear():
      container.delete_front()
      container.delete_rear()
    else:
      return f"{string} is not a palindrome"
  return f"{string} is a palindrome"

palindrome_check = is_palindrome("12321")
print(palindrome_check)
