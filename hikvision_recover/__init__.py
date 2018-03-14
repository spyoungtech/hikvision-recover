import argparse
from hikvision_recover.recover import get_code

def main():
    parser = argparse.ArgumentParser(description='Generates recovery key for Hikvision cameras')
    parser.add_argument('serial', help='Camera Serial Number')
    parser.add_argument('year', help='4 digit year of current camera time')
    parser.add_argument('month', help='2 digit month of current camera time')
    parser.add_argument('day', help='2 digit day of current camera time')
    args = parser.parse_args()

    recovery_code = get_code(args.serial, args.year, args.month, args.day)
    print(recovery_code)


if __name__ == "__main__":
    main()
