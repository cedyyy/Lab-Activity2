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

    
if avg>=99 and avg>=100:
    print("Your Grade is A")
elif avg>=90 and avg<=98:
    print("Your Grade is B")
elif avg>=80 and avg<=89:
    print("Your Grade is C")
elif avg>=71 and avg<=79:
    print("Your Grade is D")
elif avg>=61 and avg<=70:
    print("Your Grade is E")
elif avg<=60:
    print("Your Grade is F")
else:
    print("INVALID")
