import random


def num_gen():
    generated = []
    count = 0
    while count < 3:
        num = random.randint(1, 9)
        if num not in generated:
            generated.append(num)
            count += 1
    return generated


def hint(num1, num2):
    if num1 == num2:
        return 1
    count = range(3)
    for n in count:
        if num1[n] == num2[n]:
            return 2
    for n in count:
        if num1[n] in num2 or num2[n] in num1:
            return 3
    return 0


number = num_gen()
guess = []
while number != guess:
    guess.clear()
    while len(set(guess)) != 3:
        guess.clear()
        inp = input('Please enter 3 digit number with no repeating digits: ')
        for num in inp:
            guess.append(int(num))
    hint_check = hint(number, guess)
    if hint_check == 1:
        print("Congratulations, you've guessed right!")
    elif hint_check == 2:
        print("Match")
    elif hint_check == 3:
        print("Close")
    else:
        print("Nope")
