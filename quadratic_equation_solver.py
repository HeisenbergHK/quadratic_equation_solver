import math


def calculate_delta(a, b, c):
    """This function calculate delta"""
    return b ** 2 - 4 * (a * c)


def first_answer(a, b, c, delta):
    """This function calculate the first answer based on the general formula"""
    if delta < 0:
        real = -b / 2 * a
        img = math.sqrt(-delta) / 2 * a
        return [real, img]
    elif a == 0:
        real = -c / b
        return [real]
    else:
        x_top = -b + math.sqrt(delta)
        x_bot = 2 * a
        real = x_top / x_bot
        return [real]


def second_answer(a, b, c, delta):
    """This function calculate the first answer based on the general formula"""
    if delta < 0:
        real = -b / 2 * a
        img = math.sqrt(-delta) / 2 * a
        return [real, -img]
    elif a == 0:
        real = -c / b
        return [real]
    else:
        x_top = -b - math.sqrt(delta)
        x_bot = 2 * a
        real = x_top / x_bot
        return [real]


def show_result(x1, x2, delta1, a):
    """This function will show the result in a proper format"""
    print("")  # We use this empty print statement for styling the output in terminal

    if a == 0:
        print(f"\tx: {x1[0]}")
    elif x1 == x2:
        print(f"Delta is \"{delta}\".\n")
        print(f"\tx: {x1[0]}")
    elif delta < 0:
        print(f"Delta is \"{delta}\", we have complex numer for x.\n")
        print(f"\tx1: {x1[0]} + {x1[1]}i")
        print(f"\tx2: {x2[0]} - {-x2[1]}i")
    else:
        print(f"\tx1: {x1[0]}")
        print(f"\tx2: {x2[0]}")


# Ask the user for a, b, c in the equation
prompt = 'Welcome to name solver\n'
prompt += '-------------------------\n'
prompt += 'We solve an equation in the form of aX^2 + bX + c = 0'
print(prompt)

# We use a flag for the while loop to make sure user is satisfied with it`s inout
getting_active = True

# We use this while loop to get a, b, c, from the user
while getting_active:
    prompt = '\n\tEnter a: '
    a = input(prompt)
    a = int(a)

    prompt = '\tEnter b: '
    b = input(prompt)
    b = int(b)

    prompt = '\tEnter C: '
    c = input(prompt)
    c = int(c)

    print(f'\nYour equation: {-a}X^2 + {b}X + {c} = 0')

    user_input = input('\n\tIs it okay? (yes/no): ')

    # If the user is satisfied with it`s input the flag will deactivate and the loop won`t run anymore
    if user_input.lower() == 'yes':
        getting_active = False

# We need delta to use in the general formula to solve the equation
delta = calculate_delta(a, b, c)
x1 = first_answer(a, b, c, delta)
x2 = second_answer(a, b, c, delta)

# We now show the result in a proper format in the terminal
show_result(x1, x2, delta, a)
