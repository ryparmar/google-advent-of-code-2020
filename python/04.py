import argparse
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-i', type=str, help='input file')
    args = parser.parse_args()

    with open(args.i, 'r') as f:
        # data = [str(field) [passport for i, passport in enumerate(f.read().split('\n\n')) for field in passport.replace('\n', ' ').split()]
        data = [{str(field).split(':')[0]: str(field).split(':')[1] for field in passport.replace(
            '\n', ' ').split()} for passport in f.read().split('\n\n')]
        print(data)

    oblig_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl',
                    'ecl', 'pid')  # 'cid' not obligatory
    valid_passports = 0

    for passport in data:
        if (all([field in passport.keys() for field in oblig_fields])):
            valid_passports += 1
            print(passport.keys())

    print(f"Task 1: Valid Passports: {valid_passports}")

    # Validations for Task 2
    def byr_val(x):
        return len(str(x)) == 4 and 1920 <= int(x) <= 2002

    def iyr_val(x):
        return len(str(x)) == 4 and 2010 <= int(x) <= 2020

    def eyr_val(x):
        return len(str(x)) == 4 and 2020 <= int(x) <= 2030

    def hgt_val(x):
        if x[-2:] == 'cm':
            return 150 <= int(x[:-2]) <= 193
        elif x[-2:] == 'in':
            return 59 <= int(x[:-2]) <= 76

    def hcl_val(x):
        return True if re.match('#([0-9a-f]{6})', x) else False

    def ecl_val(x):
        return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def pid_val(x):
        return len(str(x)) == 9

    valid_passports2 = 0
    for passport in data:
        print(passport)
        # field must be present and valid
        if all([field in passport and eval(f"{field}_val('{passport[field]}')") for field in oblig_fields]):
            # print(f"{field in passport}")
            # print(f"{field}_val('{passport[field]}')")
            valid_passports2 += 1
            print("VALID:")

    print(f"Task 2: Valid Passports: {valid_passports2}")
