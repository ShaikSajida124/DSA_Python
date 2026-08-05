#import stack class
def matching_parentheses(string):
  stack = Stack()
  opening_brackets = "[{(<"
  closing_brackets = ">)}]"
  for char in string:
    if char in opening_brackets:
      stack.push(char)
    elif char in closing_brackets:
      if len(stack) == 0:
        return "Invalid"
      pop_item = stack.pop()
      if pop_item == "[":
        if char != "]":
          return "Invalid"
      elif pop_item == "{":
        if char != "}":
          return "Invalid"
      elif pop_item == "(":
        if char != ")":
          return "Invalid"
      elif pop_item == "<":
        if char != ">":
          return "Invalid"
  if len(stack) == 0:
    return "Valid"
  return "Invalid"
#Driver Code
test_matching_parentheses = matching_parentheses("{}()[]aaa")
print(test_matching_parentheses)

def valid_parentheses(string):
  stack = Stack()
  parentheses = {
    '[' : ']',
    '{' : '}',
    '(' : ')',
    '<' : '>'
  }
  closing_parentheses = {']', '}', ')', '>'}

  for char in string:
    if char in parentheses:
      stack.push(char)
    elif char in closing_parentheses:
      if stack.is_empty():
        return 'Invalid'
      else:
        pop_item = stack.pop()
        if parentheses.get(pop_item) != char:
          return 'Invalid'
  if stack.is_empty():
    return 'Valid'
  return 'Invalid'
#Driver Code
func_test = valid_parentheses("[[[s{(a)}j]i]]d")
print(func_test)
