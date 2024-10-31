import os
import time
import random

# ANSI escape codes for colors and styles
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_title():
    title = f"""
{BLUE}{BOLD}        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/

{MAGENTA}               {BOLD}H4CKER_2097 TOOL{RESET}
{YELLOW}==================================================
    {CYAN}{BOLD}Welcome to the H4CKEr6_2097 TOOL!{RESET}
"""
    print(title)

def get_input(prompt):
    return input(f"{CYAN}{BOLD}{prompt}{RESET}")

def choose_platform():
    print(f"{YELLOW}Please select a platform to report on:{RESET}")
    print(f"  {CYAN}1{RESET}: Telegram")
    print(f"  {CYAN}2{RESET}: Instagram")
    
    while True:
        platform = get_input("Enter your choice (1 or 2): ")
        if platform in ['1', '2']:
            return platform
        else:
            print(RED + "Invalid selection. Please choose 1 or 2." + RESET)

def choose_report_type():
    print(f"{YELLOW}Select the type of report you want to file:{RESET}")
    print(f"  {CYAN}1{RESET}: Abuse")
    print(f"  {CYAN}2{RESET}: Scammer")
    print(f"  {CYAN}3{RESET}: Spam")
    
    while True:
        report_type = get_input("Enter your choice (1, 2, or 3): ")
        if report_type in ['1', '2', '3']:
            return report_type
        else:
            print(RED + "Invalid selection. Please choose 1, 2, or 3." + RESET)

def validate_username(username):
    return username.startswith('@')

def validate_user_id(user_id):
    return user_id.isdigit() and len(user_id) == 10

def loading_animation():
    print(f"{CYAN}Submitting your report", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(RESET)

def report_tool():
    clear_screen()
    print_title()
    
    # Step 1: Choose platform
    platform = choose_platform()
    
    # Step 2: Get username
    while True:
        username = get_input("Please provide the usernam: ")
        if validate_username(username):
            break
        else:
            print(RED + "Invalid username." + RESET)
    
    # Step 3: Get user ID
    while True:
        user_id = get_input("Please provide the user ID : ")
        if validate_user_id(user_id):
            break
        else:
            print(RED + "Invalid user ID. It must be exactly 10 digits." + RESET)
    
    # Step 4: Choose type of report
    report_type = choose_report_type()
    
    # Step 5: Confirmation
    report_types = { '1': 'Abuse', '2': 'Scammer', '3': 'Spam' }
    print(f"\n{YELLOW}You are reporting the following:{RESET}")
    print(f"- Platform: {'Telegram' if platform == '1' else 'Instagram'}")
    print(f"- Username: {username}")
    print(f"- User ID: {user_id}")
    print(f"- Report Type: {report_types[report_type]}")
    
    confirm = get_input("Do you want to submit this report? (y/n): ").lower()
    
    if confirm == 'y':
        for report_number in range(1, 101):  # Report loop from 1 to 100
            loading_animation()
            print(GREEN + f"Report {report_number}: Submitted successfully!" + RESET)
            time.sleep(random.uniform(0.2, 0.8))  # Shorter random delay
            
            # Show ID ban message randomly after report number 30
            if report_number >= 30 and random.random() < 0.2:  # 20% chance
                print(RED + f"ID {user_id} banned successfully!" + RESET)
                break  # Exit the loop after banning
        else:
            print(GREEN + "All reports submitted successfully!" + RESET)
    else:
        print(RED + "Report submission canceled." + RESET)

    # Wait before exiting
    time.sleep(2)

if __name__ == "__main__":
    report_tool()
