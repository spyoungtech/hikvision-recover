import argparse

def rshift(val, n):
    return (val % 0x100000000) >> n

def get_code(serial, year, month, day):
    magic_number = 0
    serial = serial + year + month + day
    for index, char in enumerate(serial):
        magic_number += ord(char) * (index + 1) ^ (index + 1)

    magic_number *= 1751873395
    magic_number = rshift(magic_number, 0)
    magic_word = str(magic_number)

    serial_code = ""

    for char in magic_word:
        c = ord(char)

        if c < 51:
            serial_code += chr(c + 33)
        elif c < 53:
            serial_code += chr(c + 62)
        elif c < 55:
            serial_code += chr(c + 47)
        elif c < 57:
            serial_code += chr(c + 66)
        else:
            serial_code += chr(c)
    return serial_code

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates recovery key for Hikvision cameras')
    parser.add_argument('serial', help='Camera Serial Number')
    parser.add_argument('year', help='4 digit year of current camera time')
    parser.add_argument('month', help='2 digit month of current camera time')
    parser.add_argument('day', help='2 digit day of current camera time')
    args = parser.parse_args()

    serial = get_code(args.serial, args.year, args.month, args.day)
    print(serial)