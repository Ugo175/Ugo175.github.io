class BaseConverter:
    
    def __init__(self):
        self.base_map = {
            2: self.nbase_to_decimal,
            10: self.decimal_to_nbase,
            16: self.nbase_to_decimal,
        }
        self.reverse_map = {
            "decimal": self.decimal_to_nbase,
            "binary": self.nbase_to_decimal,
            "hexa": self.nbase_to_decimal,
        }

    def decimal_to_nbase(self, number, base_n):
        if base_n == 10:
            return number
        
        if not (2 <= base_n <= 16):
            raise ValueError("Inputted base must be between 2 and 16")
        
        extra_digits = "0123456789ABCDEF"
        remainders = []
        
        while number > 0:
            remainders.append(str(number % base_n)) 
            number //= base_n
            
        if base_n < 10:
            return "".join(remainders[::-1])
        else:
            output = [extra_digits[int(i)] for i in remainders[::-1]]
            return "".join(output)


    def nbase_to_decimal(self, number, base_n):
        if base_n == 10:
            return number

        if not (2 <= base_n <= 16):
            raise ValueError("Inputted base must be between 2 and 16")

        nim = []
        flipped = str(number)[::-1]
        extra_digits = "0123456789ABCDEF"
            
        if base_n < 10:
            for i in range(len(str(number))):
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

    def hexa_to_binary(self, number, base_n=16):
        if base_n != 16:
            raise ValueError("Inputted base must be 16")

        extra_digits = "0123456789ABCDEF"
        binary_map = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
                        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
                        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
                        "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

        binary_string = ""
        for char in number.upper(): 
            if char not in extra_digits:
                
                raise ValueError(f"Invalid character '{char}' for base {base_n}")
            
            binary_string += binary_map[char]

        return binary_string.zfill(len(number) * 4)  

    def binary_to_hexa(self, number, base_n=2):
        if base_n != 2:
            raise ValueError("Inputted base must be 2")

        binary_map = {"0000": "0", "0001": "1", "0010": "2", "0011": "3",
                    "0100": "4", "0101": "5", "0110": "6", "0111": "7",
                    "1000": "8", "1001": "9", "1010": "A", "1011": "B",
                    "1100": "C", "1101": "D", "1110": "E", "1111": "F"}


        binary_length = len(str(number))
        remainder = binary_length % 4
        if remainder != 0:
            number = '0' * (4 - remainder) + str(number)

        hexa_string = ""
        for i in range(0, len(number), 4):
            chunk = number[i:i+4]
            hexa_string += binary_map[chunk]

        return hexa_string

    def convert(self, number, from_base, to_base):
        """Converts a number from one base to another."""
        if not (2 <= from_base <= 16 and 2 <= to_base <= 16):
            raise ValueError("Bases must be between 2 and 16")

        if from_base in self.base_map:
            number = self.base_map[from_base](number, 10)

        return self.base_map[to_base](number, to_base)


converter = BaseConverter()
print(converter.convert(123, 10, 2))  # Output: 1111011
print(converter.convert("6BA", 16, 2))  # Output: 110101010
print(converter.convert(1011011, 2, 16))  # Output: B3
