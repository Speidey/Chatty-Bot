def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name(name):
    print('Please, remind me of your name.')
    print('What a great name you have, ' + name + '!')


def guess_age(rem3, rem5, rem7):
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count(num):
    print('Now I will prove to you that I can count to any number you want.')

    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')

    if int(input()) != 2:
        print('Please, try again.')
        int(input())
    else:
        print('Congratulations, have a nice day!')



def end():
    print('Congratulations, have a nice day!')


greet('Jarvis', '2022')  # change it as you need
remind_name('Paul')
guess_age(0, 4, 3)
count(3)
test()
end()
