

def daily_reminder():
    # Prompt for the task description
    task = input("Enter your task: ")
    #
    # 
    # Prompt for priority level
    priority = input("Priority (high/medium/low): ").lower()
    
    # Prompt for time sensitivity
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Validating input for priority and time_bound
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
        return

    if time_bound not in ["yes", "no"]:
        print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
        return
    
    # Customized reminder message based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
    
    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Print the customized reminder
    print("Reminder:", reminder)

# Run the function
if name == "main":
    daily_reminder()
