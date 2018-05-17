#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers#

num1=999;
num2=999;
palindromes=[];
prod=num1*num2
while num1>=100:
	if str(prod)==str(prod)[::-1]:
		palindromes.append(prod)
	num2-=1;
	if num2 < 100:
		num2=999;
		num1-=1;
	prod=num1*num2;
print(max(palindromes))
