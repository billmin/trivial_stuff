def mye(level):
	if level < 1:
		raise Exception("Invalid level!")

try:
	mye(0)
except Exception as err:
	print(1, err)
else:
	print(2)
