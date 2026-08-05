history_file = "history.txt"

def history():
    file = open(history_file, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("INVALID OUTPUT !!!, ADD NUMBERS FIRST")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear():
    file = open(history_file, "w")
    file.close()
    print("DATA CLEARED SUCCESSFULLY")

def save(equation, result):
    file = open(history_file, "a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("INVALID ENTRY")
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
        result = num1 / num2
    else:
        print("INVALID NUMBER OPERATOR")
        return

    if int(result) == result:
        result = int(result)

    print("RESULT :", result)
    save(user_input, result)

def main():
    print("--- SIMPLE CALCULATOR WITH HISTORY, CLEAR, EXIT ---")

    while True:
        user_input = input("ENTER THE CALCULATION (+,-,*,/) or command : ")

        if user_input == "exit":
            print("GOODBYE-----------")
            break
        elif user_input == "history":
            history()
        elif user_input == "clear":
            clear()
        else:
            calculate(user_input)

main()
   
