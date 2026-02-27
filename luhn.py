#!/usr/bin/env python3

def verify_card(card_number):
    sum_of_odd_digits = 0
    reversed_card_digits = card_number[::-1]
    odd_digits = reversed_card_digits[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = reversed_card_digits[1::2]

    for digit in even_digits:
        number = int(digit) * 2

        if (number>= 10):
            number = number//10 + number % 10
        sum_of_even_digits += number
    
    total = sum_of_even_digits + sum_of_odd_digits
    print(total)

    return total % 10 == 0

def main():
    card_number = "4500-4400-0195-6965"
    card_translation = str.maketrans({'-':'', ' ':''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card(translated_card_number):
        print('VALID')
    else:
        print('INVALID!')

main()
