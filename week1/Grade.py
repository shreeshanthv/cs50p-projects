score = int(input("What is your score?"))
if score < 0 or score >100:
    print("invalid score")
elif score >= 90 and score <= 100:
    print("Grade A")
elif score <= 80 and score >= 90:
    print("Grade B")
elif score <=70 and score >= 80:
    print("Grade C")
else:
    print("Grade D")

 
