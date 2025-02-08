first_number = input('Enter the first number:')
second_number = input('Enter the second number:')

def multiply(first_num, second_num):
    total = int(first_num) * int(second_num)

    print(f'{first_num} * {second_num} = {total}')

multiply(first_number, second_number)