number = int(input("Enter a number: "))
print("Multiplication Table of: " + str(number))
for i in range(11):
    print(number,'x',i,'=',number*i)