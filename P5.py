numbers=list(range(1,11));
prod=1;
for num in numbers[::-1]:
	if prod%num!=0:
		prod*=num;
print(prod)