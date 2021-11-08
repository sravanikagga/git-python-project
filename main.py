def ispalindrome(s):
	return s== s[::-1]
s="malayalam"
ans =ispalindrome(s)
if ans:
	print("yes")
else:
	print("no")