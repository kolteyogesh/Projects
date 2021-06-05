Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string
>>> import random
>>> def randompassword():
	chars = string.ascii_letters + string.digits
	size = 3
	return ''.join(random.choice(chars)for x in range(size,27))

>>> n = 0
>>> while n < 50:
	print(randompassword())
	n = n + 1
	