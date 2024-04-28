def dec_to_base(num, base):
    """Convert decimal to other bases"""
    if base == 2:
        return bin(num)[2:]
    elif base == 8:
        return oct(num)[2:]
    elif base == 16:
        return hex(num)[2:].upper()
    else:
        return str(num)

def base_to_dec(num, base):
    """Convert other bases to decimal"""
    return int(str(num), base)

def number_system_converter():
    print("Welcome to Number System Converter")
    print("1. Forward Convert")
    print("2. Backward Convert")
    print("3. Vertical Convert")
    choice = input("Enter your choice: ")

    if choice == '1':
        num = int(input("Enter the number: "))
        base = int(input("Enter the base of the number (2, 8, 10, 16): "))
        result = [dec_to_base(num, b) for b in (2, 8, 10, 16)]
        print(f"Decimal: {result[2]}, Binary: {result[0]}, Octal: {result[1]}, Hexadecimal: {result[3]}")
    elif choice == '2':
        num = input("Enter the number: ")
        base = int(input("Enter the base of the number (2, 8, 10, 16): "))
        result = base_to_dec(num, base)
        print(f"Decimal: {result}")
    elif choice == '3':
        num = input("Enter the number: ")
        base = int(input("Enter the base of the number (2, 8, 10, 16): "))
        if base == 10:
            print(f"Decimal: {num}")
        else:
            print(f"Decimal: {base_to_dec(num, base)}, Binary: {dec_to_base(base_to_dec(num, base), 2)}, Octal: {dec_to_base(base_to_dec(num, base), 8)}, Hexadecimal: {dec_to_base(base_to_dec(num, base), 16)}")
    else:
        print("Invalid choice")

number_system_converter()
