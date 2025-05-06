def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def main():
    print("Temperature Converter")
    print("1: Fahrenheit to Celsius")
    print("2: Celsius to Fahrenheit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F is equal to {c:.2f}°C")
    elif choice == "2":
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {f:.2f}°F")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Required line to call main()
if __name__ == '__main__':
    main()
