age1=int(input("Enter first person's age:"))
age2=int(input("ENter Second person's age:"))
age3=int(input("Enter Third person's age"))
old,young=0,0
if age1>=age2 and age1>=age3:
	oldest=1
	if age2>=age3:
		youngest=3
	else:
		youngest=2
if age2>=age1 and age2>=age3:
	oldest=2
	if age1>=age3:
		youngest=3
	else:
		youngest=1
if age3>=age2 and age3>=age1:
	oldest=3
	if age2>=age1:
		youngest=1
	else:
		youngest=2
print("Oldest is Person{0} and Youngest is Person{1}".format(oldest,youngest))
