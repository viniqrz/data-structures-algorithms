# Decode String: E.g., parsing "3[a2[c]]" into "accaccacc".
# You use a stack to remember the multiplier
# and the string built so far before diving into the inner brackets.

def decode(text: str):
  res = []
  i = 0

  currNum = 0
  currNumSubstr = ''

  currSubstr = ''

  while i < len(text):
    char = text[i]

    if char == '[':
      currNum = int(currNumSubstr)
      currNumSubstr = ''

    if char == ']':
      res.append(currNum * currSubstr)
      currSubstr = ''
      return ''.join(res), i + 1

    if char.isdigit():
      if currNum > 0:
        seq, delta = decode(text[i:])
        currSubstr += seq
        i = i + delta
        continue
      else:
        currNumSubstr += char

    if not char.isdigit() and not char in ['[', ']']:
      currSubstr += char

    i += 1

  return ''.join(res)

print(decode('3[a2[c]]')[0] == 'accaccacc')