task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ").lower()
time_bound=input("Is it time-bound? (yes/no): ").lower()

if time_bound == 'yes' :
    reminder = (f"Reminder: '{task}' is a high priority task")
else:
      reminder = (f"Note: '{task}' is a low priority task")

match priority:
    case "high":
        if time_bound == 'yes':
             reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider completing it when you have free time."
    case "medium":
        if time_bound == 'yes':
             reminder += " that requires immediate attention today!"
        else:
             reminder += ". Consider completing it when you have free time."
    case "low":
        if time_bound == 'yes':
             reminder += " that requires immediate attention today!"
        else:
             reminder += ". Consider completing it when you have free time."

print(reminder)