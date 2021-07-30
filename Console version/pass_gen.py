'''

title: a simple password generator
to run on the console

'''
from random import choice


def generate_password():
    numbers = '0123456789'
    alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_alpha_num = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'!@$%()?"

    # get the pass_length from the user
    try:

        pass_len = int(input('Enter password length: '))

        # initialize an empty list
        random_pass = []

        print('Select the type of password: \n1. Numbers\n2. Alphanum\n3.Special alphanum\n')
        select_type = int(input())

        # check the selected option

        if select_type == 1:
            for i in range(pass_len):
                random_pass.append(choice(numbers))
        elif select_type == 2:
            for i in range(pass_len):
                random_pass.append(choice(alphanum))
        elif select_type == 3:
            for i in range(pass_len):
                random_pass.append(choice(special_alpha_num))
        else:
            print('Option selected is out of range!')

            result = ''.join(random_pass)

            print('Generated password is : ' + result)

    except ValueError as e:
        print(e)


if __name__ == '__main__':
    generate_password()
