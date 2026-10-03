

def calc(input: str):
  stack = []
  i = 0
  currNum = ''

  while i < len(input):
    p = input[i]

    if p.isdigit():
      currNum += p

    if p in ['*', '/', '-']:
      stack.append(p)

    if p in [' ', ')'] or i == len(input) - 1:
      if currNum:
        if not stack:
          stack.append(int(currNum))
        elif stack[-1] == '/':
          stack.pop()
          last = stack.pop()
          stack.append(last / int(currNum))
        elif stack[-1] == '*':
          stack.pop()
          last = stack.pop()
          stack.append(last * int(currNum))
        elif stack[-1] == '-':
          stack.pop()
          stack.append(- int(currNum))
        else:
          stack.append(int(currNum))
        currNum = ''

    if p == ')':
      return sum(stack), i + 1

    if p == '(':
      total, delta = calc(input[i+1:])
      stack.append(total)
      i = i + delta
  
    i+=1

  print(input,' = ', sum(stack))

  return sum(stack)

print(calc('1 * 2 * 3'))
print(calc('1 + 2 * 3'))
print(calc('(1 - 2) * 3'))
print(calc('((1 + (2 * 10)) * 2) * 3'))