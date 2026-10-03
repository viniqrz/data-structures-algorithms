def subadd(text: str, r = False):
  total = 0
  i = 0

  seq = ''
  op = ''

  while i < len(text):
    if text[i] == '(':
      if op:
        res, delta = subadd(text[i-3:], True)
        i = i + delta
        total += res
        seq = ''
        continue
      else:
        op = seq

      seq = ''

    if text[i] == ',':
      if seq:
        total = int(seq)
        seq = ''

    if text[i] == ')':
      if op == 'add':
        total = total + int(seq)
      if op == 'sub':
        total = total - int(seq)
      break

    if text[i].isdigit():
      seq += text[i]

    if text[i].isalpha():
      seq += text[i]
      
    i+=1

  if not r:
    return total

  return total, i

print(subadd('add(2,3)'))
print(subadd('sub(2,3)'))
print(subadd('sub(sub(2,3),add(2,3))'))