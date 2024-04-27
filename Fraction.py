def decimal_to_nbase(number, base_n):
    num = int(number)
    if base_n == 10:
        return number
  
    if not (2 <= base_n <= 16):
        raise ValueError("Inputted base must be between 2 and 16")
  
    extra_digits = "0123456789ABCDEF"
    remainders = []

    while num > 0:
        remainders.append(str(num % base_n)) 
        num //= base_n
    
    if base_n < 10:
        return "".join(remainders[::-1])
    else:
        output = [extra_digits[int(i)] for i in remainders[::-1]]
    return "".join(output)



def nbase_to_decimal(number, base_n):
 
    if base_n == 10:
        return number
 
    if not (2 <= base_n <= 16):
        raise ValueError("Inputted base must be between 2 and 16")

    nim = []
    flipped = str(number)[::-1]
    extra_digits = "0123456789ABCDEF"

    if base_n < 10:
        for i in range(len(flipped)):
            nim.append(int(base_n**i)*int(flipped[i]))
        return sum(nim)
 
    else:
        numbers = []
        for char in flipped:
            if char not in extra_digits: 
                raise ValueError(f"Invalid character '{char}' for base {base_n}")
            else:
                numbers.append(extra_digits.index(char)) 

    decimal_value = 0
    for i in range(len(numbers)):
        decimal_value += int(numbers[i]) * int((base_n**i))

    return decimal_value


while True:
    numero = (input("Enter a number: ")).upper()
    base_to = int(input("Enter the base you wish to convert to: "))
    from_base = int(input("Enter the base of the number: "))

    decimal_eq = nbase_to_decimal(numero, from_base)
    binary_eq = decimal_to_nbase(decimal_eq, 2)
    hexadecimal_eq = decimal_to_nbase(decimal_eq, 16)

    if base_to == 2:
        print(f"The binary equivalent of {numero} base {from_base} is {binary_eq}")
    elif base_to ==16:
        print(f"The hexadecimal equivalent of {numero} base {from_base} is {hexadecimal_eq}")
    elif base_to == 10:
        print(f"The decimal equivalent of {numero} base {from_base} is {decimal_eq}")

