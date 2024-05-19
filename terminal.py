import os

# Input function
def get_user_input(prompt):
    return input(prompt).strip()

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def about():
    print("""
    TWFD Terminal
    Version 1.0
    Developed by The Free Wild Dude's Team
    April 2024""")
# Calculate function
def calculate(expression):
    try:
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

# Main Function
def main():
    print("""
╭━━┳┳━┳┳━━┳━━╮
╰╮╭┫┃┃┃┃━┳┻╮╮┃
╱┃┃┃┃┃┃┃╭╯╭┻╯┃
╱╰╯╰━┻━┻╯╱╰━━╯
╭╮╱╱╱╱╱╱╱╭╮
┃╰┳━┳┳┳━━╋╋━┳┳━╮╭╮
┃╭┫┻┫╭┫┃┃┃┃┃┃┃╋╰┫╰╮
╰━┻━┻╯╰┻┻┻┻┻━┻━━┻━╯Version 1.0""")
    try:
        print("what is your name: ")
        name = get_user_input("")
        print("Your name is " + name + ". Welcome to TWFD Terminal!")
        input("Press Enter to continue")
    except Exception as e:
        print("Error", e)

    
    while True:
        print("(Use 'help' for list of commands or 'quit' to exit):")
        expression = get_user_input("Command >> ")
        if expression.lower() == 'quit':
            print("Exiting...")
            break
        elif expression.lower() == 'help':
            print("Welcome to TFWD Terminal Help Menu!")
            commands = {
                1: "help",
                2: "quit",
                3: "clear - Under Development",
                4: "about",
                5: "version",
                6: "calculate",
            }
            print(commands)
        elif expression.lower() == 'clear':
            clear_screen()
        elif expression.lower() == 'about':
            about()
        elif expression.lower() == 'version':
            print("Version 1.0")
        elif expression.lower() == 'calculate':
            print("Enter an arithmetic expression: ")
            expression = get_user_input("")
            calculate(expression)
        else:
            print("Invalid command. Please try again.")


main()

