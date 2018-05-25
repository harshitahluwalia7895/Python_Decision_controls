sex=input("Enter sex(M or F): ")
ms=input("Enter marital status(Y or N): ")
age=int(input("Enter age of Employee: "))

if sex=='F':
	if age>20 and age<=60:
		print("Employee will work only in urban areas")
	else:
		print("ERROR")
elif sex=='M':
	if age>20 and age<=40:
		print("Employee can work anywhere")
	elif age>40 and age<=60:
		print("Employee will work only in urban areas")
	else:
		print("ERROR")

