# PROJECT 2 ---> Tip calculator 

def welcome_statement():
    print("Welcome to the Tip Calculator")

welcome_statement()
bill = float(input("Enter a Bill: $"))
tips = int(input("What percentage tip would you like to give ? 10 ,12 or 15: "))
split_bill = int(input("Enter a number of the person you want to split the bill between: "))
total_bill = bill + (tips/100)*bill
each_person_bill = round(total_bill/split_bill, 2)
print(f"Each Person should pay ${each_person_bill} and your final is ${total_bill}")