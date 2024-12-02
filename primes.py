# super simple prime generator based on the sieve of eratosthenes
def primegen(max):
	ar = [0 for x in range(max)]
	ar[0], ar[1] = 1, 1 #eliminate base cases
	for i in range(len(ar)):
		if ar[i] == 0:
			yield i
			ar[i::i] = [1 for x in range(0, len(ar[i::i]))]

This is a test!

def somerandomfucntion(variable):
	print(variable)
