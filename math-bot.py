# Input function
def get_user_input(prompt):
    return input(prompt).strip()

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
█████████████████████████████████████████████████████████
██▀▄─██▄─▄▄▀█▄─▄█─▄─▄─█─█─█▄─▀█▀─▄█▄─▄▄─█─▄─▄─█▄─▄█─▄▄▄─█
██─▀─███─▄─▄██─████─███─▄─██─█▄█─███─▄█▀███─████─██─███▀█
▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▄▀▀▄▀▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀
██████████████████████████████████████████████████████████████████████████
█─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▄█▄─▀█▀─▄█▄─██─▄█▄─▄████▀▄─██─▄─▄─█─▄▄─█▄─██─▄█▄─▄▄▀█
███─████─▄█▀██─▄─▄██─███─█▄█─███─██─███─██▀██─▀─████─███─██─██─██─███─▄─▄█
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀ Version 1.0""")
    try:
        print("what is your name: ")
        name = get_user_input("")
        print("Your name is " + name + ".")
    except Exception as e:
        print("Error", e)

    
    while True:
        print("Enter an arithmetic expression (or 'quit' to exit):")
        expression = get_user_input("")
        if expression.lower() == 'quit':
            print("Exiting...")
            break
        else:
            calculate(expression)


main()
