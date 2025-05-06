def main():
    # Prompt the user for the lengths of the sides
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Display the result
    print("The perimeter of the triangle is", perimeter)

if __name__ == "__main__":
    main()
