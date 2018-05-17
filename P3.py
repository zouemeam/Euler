#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

number=600851475143;
d=2;
factor=[];
while number>1:
	while number%d==0:
		factor.append(d);
		number/=d;
	d+=1;
print(factor)