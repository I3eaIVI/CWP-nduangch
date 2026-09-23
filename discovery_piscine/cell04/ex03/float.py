num = input("Give me a number: ")
num_f = float(num)
if num_f.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")