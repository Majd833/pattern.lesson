row=int(input("Enter the number of rows that you want in your floyd's triangle:"))
number=0

print("Floyd's Triangle:")
for i in range(1,row+1):
    for j in range(1,i+1):
        number=number+1
        print(number,end="")
    print("")