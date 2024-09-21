task=input("Enter your task: ")
task_priority=input("Priority (high/medium/low): ").lower()
time_bound=input("Is it time-bound? (yes/no): ").lower()

match task_priority:
    case "high":
        if time_bound == 'no':
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        else:
            reminder = f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!"
    case "medium":
        if time_bound == 'no':
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        else:
             reminder = f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!"
    case "low":
        if time_bound == 'no':
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        else:
            reminder = f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!"

print(reminder)