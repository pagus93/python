
def switch(choice, inputs, outputs):
    for i in range(0, len(inputs)):
        if choice == inputs[i]:
            if outputs[i] == 'break':
                break
            if outputs[i] == 'continue':
                continue
            else:
                return outputs[i]
    return None

def operation(x, sign, y):
    if sign == "+":
        return float(x)+float(y)
    elif sign == "-":
        return float(x)-float(y)
    elif sign == "*":
        return float(x)*float(y)
    elif sign == "/":
        return float(x)/float(y)
    elif sign == "**":
        return float(x)**float(y)
    else:
        return None

choice = ""
inputs = ["+", "-", "*", "/", "quit"]
outputs = ["plus", "minus", "times", "over", "break"]

while choice != "quit":
    print("Options:")
    for i in range(0, len(inputs)):
        print(str(i+1) + ". " + inputs[i])
    choice = input("Insert your choice: ")
    print(switch(choice, inputs, outputs))
