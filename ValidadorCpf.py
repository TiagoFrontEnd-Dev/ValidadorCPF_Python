import re
import sys
user_input = input('Digite Seu CPF: ')
user_cpf = re.sub(
    r'[^0-9]',
    '',
    user_input
)
sequential_inpunt = user_input == user_input[0] * len(user_input)

if sequential_inpunt:
    print('Você enviou dados sequenciais.')
    sys.exit()


nine_digit = user_cpf[:9]
regressive_counter_one = 10

result_digit_one = 0
for digit in nine_digit:
    result_digit_one += int(digit) * regressive_counter_one
    regressive_counter_one -= 1

one_digit = (result_digit_one * 10) % 11
one_digit = one_digit if one_digit <= 9 else 0 

ten_digit = nine_digit + str(one_digit)
regressive_counter_two = 11

result_digit_two = 0
for digit in ten_digit:
    result_digit_two += int(digit) * regressive_counter_two
    regressive_counter_two -= 1
two_digit = (result_digit_two * 10) % 11
two_digit = two_digit if two_digit <= 9 else 0 

new_cpf = f'{nine_digit}{one_digit}{two_digit}'

if user_cpf == new_cpf:
    print(f'\nO CPF {user_cpf} é VÁLIDO\n')
else:
    print('CPF inválido')