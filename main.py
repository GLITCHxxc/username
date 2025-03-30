import random
import string
from colorama import Fore, Style, init
import time  # Import time module for delay

# Initialize colorama
init(autoreset=True)

def generate_usernames():
    # Display the banner with colors
    print(Fore.CYAN + """  
     ██████╗ ██╗     ██╗ ██████╗██╗  ██╗██╗  ██╗
    ██╔════╝ ██║     ██║██╔════╝██║  ██║╚██╗██╔╝
    ██║  ███╗██║     ██║██║     ███████║ ╚███╔╝ 
    ██║   ██║██║     ██║██║     ██╔══██║ ██╔██╗ 
    ╚██████╔╝███████╗██║╚██████╗██║  ██║██╔╝ ██╗
     ╚═════╝ ╚══════╝╚═╝ ╚═════╝╚═╝  ╚══╚═╝  ╚═╝
    """ + Style.RESET_ALL)

    # Display the free version message in English
    print(Fore.YELLOW + "🎉 Welcome to the Free Version of the Username Generator Tool!")
    print("This tool generates Discord usernames for you. Enjoy using it!" + Style.RESET_ALL)

    # Ask the user how many usernames they want, with color
    num_users = int(input(Fore.YELLOW + "📌 How many usernames do you want? " + Style.RESET_ALL))

    # Function to generate a random username
    def generate_username():
        # Create a random username with 2 random letters and 2 random digits
        letters = ''.join(random.choices(string.ascii_letters, k=2))
        digits = ''.join(random.choices(string.digits, k=2))
        return f"{letters}{digits}"

    # Generate the usernames
    usernames = [generate_username() for _ in range(num_users)]

    # Display the generated usernames with the same color
    print(Fore.GREEN + "\n🎭 Generated Usernames:" + Style.RESET_ALL)
    for username in usernames:
        # Use the same color for all usernames
        print(Fore.GREEN + username + Style.RESET_ALL)
        
        # Add delay for smoother display
        time.sleep(0.3)  # 0.3 seconds delay between each username

    # Create and write the usernames to a txt file
    with open("genusernames.txt", "w") as file:
        for username in usernames:
            file.write(username + "\n")

    print(Fore.GREEN + "\nUsernames have been written to 'genusernames.txt'" + Style.RESET_ALL)

# Run the username generation function
generate_usernames()

# Ask the user if they want to restart or exit
while True:
    choice = input(Fore.CYAN + "\nPress 1 to restart or 2 to exit: " + Style.RESET_ALL)
    if choice == "1":
        # Restart the program by calling the function again
        generate_usernames()
    elif choice == "2":
        # Exit the program
        print(Fore.RED + "Exiting... Goodbye!" + Style.RESET_ALL)
        break
    else:
        print(Fore.YELLOW + "Invalid choice! Please press 1 to restart or 2 to exit." + Style.RESET_ALL)
