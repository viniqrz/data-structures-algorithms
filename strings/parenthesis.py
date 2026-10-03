def validParen(input):
	
	i = 0
	
	map = {
		')': '(',
		'}': '{',
		']': '[',
	}
	
	stack = []
	
	while i < len(input) - 1:
		p = input[i]

		if p in map.values():
			stack.append(p)
			
		if p in map:
			if len(stack) == 0:
				return False
		
			popped = stack.pop()

			print(popped, p)
			
			if popped != map[p]:
				return False, 'error at index ' + str(i)

		i+=1
	
	return True


# TEST
print(validParen('[{({({[]}))}]'))
print(validParen('[{(({[]}))}]'))
print(validParen('[{(({[]}))}]'))