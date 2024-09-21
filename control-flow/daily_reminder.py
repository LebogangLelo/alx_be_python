task=input("Enter your task: ")
task_priority=input("Priority (high/medium/low): ")
time_bound=input("Is it time-bound? (yes/no): ")
match task_priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        print(f"Reminder: '{task}' is am medium priority task that requires some attention this week.")
    
if time_bound=='no':
    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")