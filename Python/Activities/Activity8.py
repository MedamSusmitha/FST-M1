numbers = list(input("Enter a sequence of comma separated values: ").split(","))
print("Given Numbers are" , numbers)
print(numbers[:1])
print(numbers[-1:])
Felement=numbers[0]
Lelement=numbers[-1]
if (Felement==Lelement):
   print("True")
else :
   print("Flase")