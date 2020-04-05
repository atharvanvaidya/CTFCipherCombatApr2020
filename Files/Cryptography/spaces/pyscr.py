f = open("decodedSpaces.txt", "rt")
line = f.read()
# print(line)
lines = line.split('\n')
for x in lines:
	# print(x)
	indLine = x.split('space')
	print(indLine)
