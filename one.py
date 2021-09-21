print("Enter Marks Obtained in the whole se ")
print("Prelim")
pre = int(input())
print("Midterm")
mid = int(input())
print("Semis")
semis = int(input())
print("Finals")
fina = int(input())


tot = pre + mid + semis + fina
avg = tot/4

if avg >=75:
    print(" You Passed ")
else :
    print("You Failed")