from scicalculator import add, subtract, multiply, divide, exponent, factorial, square

def getinput(prompt):
    return float(input(prompt))

def nonegainput(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) >= 0:
            return int(value)
        else:
            print("Silvouple antre on nonb antye ki pozitif.")

def main():
    print("-Seleksyone operasyon ou vle an-")
    print("1. Adisyon")
    print("2. Subtraksyon")
    print("3. Miltiplikasyon")
    print("4. Divizyon")
    print("5. Exponansyel")
    print("6. Faktoryel")
    print("7. Rasin kare")

    choice = input("\nAntre nimero ou vle an (1-7): ")

    if choice in ['1', '2', '3', '4']:
        num1 = getinput("Antre premye chif la: ")
        num2 = getinput("Antre dezyem chif la: ")
    elif choice == '5':
        num1 = getinput("Antre chif la: ")
        num2 = getinput("Antre eksponan an: ")
    elif choice == '6':
        num1 = nonegainput("Antre chif la (on nonb antye pozitif): ")
        num2 = None
    elif choice in ['7']:
        num1 = getinput("Antre chif la: ")
        num2 = None
    else:
        print("Chwa ou an pa bon!!!")
        return

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = exponent(num1, num2)
    elif choice == '6':
        result = factorial(num1)
    elif choice == '7':
        result = square(num1)

    print("Result:", result)

if __name__ == "__main__":
    main()
