HISTORY_FILE = "history.txt"

def show_history():
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
    if len(lines) == 0:
        print("No History found!")
    else:
        for line in reversed(lines):
            print(line.strip())

def clear_history():
    open(HISTORY_FILE, 'w').close()
    print('History cleared.')

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format: number operator number (e.g., 9 + 9)')
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print('Cannot divide by zero')
            return
        result = num1 / num2
    else:
        print('Invalid Operator. Use only + - * /')
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print('_______ SIMPLE CALCULATOR (type history, clear or exit) _______')
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear): ")
        if user_input == 'exit':
            print('GoodBye!')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()
