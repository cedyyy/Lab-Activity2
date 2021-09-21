print("Enter Marks Obtained in the whole sem ")
print("PRELIMS ")
pre = int(input())
print("MIDTERMS ")
mid = int(input())
print("SEMIS-FINALS")
semis = int(input())
print("FINALS")
fina = int(input())


tot = pre + mid + semis + fina
avg = tot/4

if avg>=75:
    print("You're so awesome you passed")
elif avg<75:
    print("it's okay better luck next time")
else:
    print("Invalid Input!!!")