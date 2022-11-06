#Armstrong Number ?
number = int(input("Armstrong ? :"))
counter = 0
for i in list(str(number)):
    counter += int(i)**len(list(str(number)))
if counter == number:
    print("{} is a Armstrong number".format(number))
else:
    print("{} isn't a Armstrong number".format(number))