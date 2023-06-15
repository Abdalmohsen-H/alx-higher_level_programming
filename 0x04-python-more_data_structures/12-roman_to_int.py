#!/usr/bin/python3
def roman_to_int(roman_string):
    # task 12 interview question : roman to decimal converter
    # if !(isinstance(roman_string, str)):  # better for type checking 
    if type(roman_string) != str or roman_string is None:
        return 0
    total = 0
    convrt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for indx, romchar in enumerate(roman_string):
        # print(f"roman string {indx}, {romchar}")
        for rom, dec in convrt.items():
            # print(f"convrt {rom}, {dec}")
            if romchar == rom:
                # cuurent roman char
                deccrntrom = convrt[roman_string[indx]]
                # check if roman string still have next chars
                if indx+1 < len(roman_string):
                    decnxtrom = convrt[roman_string[indx+1]]
                    if decnxtrom > deccrntrom:
                        total = total - deccrntrom
                    else:
                        total += deccrntrom
                else:
                    total += deccrntrom
    return total


"""
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
"""
