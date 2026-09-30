# Daily Spending Tracker
# Tracks spending over 3 days against a $20 daily budget and a $60 total budget.

# Task 1: Variables
name = input("Enter your name: ")
total_spent = 0

print(f"Hello, {name}! Let's track your spending over 3 days.")

# Task 2: Loop once for each of the 3 days
for day in range(1, 4):
    spent = float(input(f"Day {day} - Enter money spent today ($): "))
    total_spent += spent

    if spent > 20:
        print("Over your $20 budget today!")
    else:
        print("Great! Under budget today.")

# Task 3: Final summary
print(f"Total money spent over 3 days: ${total_spent:.2f}")

if total_spent <= 60:
    print("Overall Result: You stayed under your $60 total budget!")
else:
    print("Overall Result: You went over your $60 total budget!")
