task=input("Enter your task: ")
task_priority=input("Priority (high/medium/low): ").lower()
time_bound=input("Is it time-bound? (yes/no): ").lower()

if task_priority == 'low' and time_bound == 'no':
    reminder = f"Note: '{task}' is a low priority task"
else:
    reminder = f"Reminder: '{task}' is a {task_priority} priority task"

match task_priority:
    case "high":
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
    case "medium":
         reminder+= ". Consider completing it soon."
    case "low":
         reminder+= ". Consider completing it when you have free time."
    case _:
        reminder+= "."

print(reminder)