task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ").lower()
time_bound=input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == 'yes':
             reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case "medium":
        if time_bound == 'yes':
             reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        else:
             reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case "low":
        if time_bound == 'yes':
             reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        else:
             reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

print(reminder)