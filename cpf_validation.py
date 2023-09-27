import random
import sys

def cpf_generator():
  nine_digits = ''
  for i in range(9):
    nine_digits += str(random.randint(0,9))
  return nine_digits

def sum_of_digits(cpf, counter):
  sum = 0
  for digit_str in cpf:
    sum += int(digit_str) * counter
    counter -=1
  return sum

def get_one_digit(result_sum_digits):
  rest = (result_sum_digits * 10) % 11
  return  str(0) if rest > 9 else str(rest)
   
     
def add_digit(cpf, counter):
  result_of_sum = sum_of_digits(cpf, counter)
  digit = get_one_digit(result_of_sum)
  return new_cpf + digit


def verification(cpf1, cpf2):
  if cpf1 == (cpf2[0] * 11):
    return False
  elif cpf1 != cpf2:
    return False
  else: 
    return True

def show_message(option, validation):
  if option == 1:
    print(f'CPF: {new_cpf}')
  
  if option == 2:
    if validation:
      print('CPF is valid')
    else: 
      print('CPF is not valid')

# =================================================================

print('Choose a of options')
print('1 - CPF Generate')
print('2 - CPF Validate')

input_cpf = ''
option = ''

while True:
  option = input('Option: ')
  option = int(option)
  if option == 1:
    input_cpf = cpf_generator()
    break
  elif option == 2:
    input_cpf = input_cpf = input('Enter with a CPF: ') \
      .replace('.', '') \
      .replace('-', '')
    break
  else:
    print('Invalid option')
    continue
  
new_cpf = input_cpf[:9]     
counter = 10

new_cpf = add_digit(new_cpf, counter)
counter += 1
new_cpf = add_digit(new_cpf, counter)

validation = verification(input_cpf, new_cpf)
show_message(option, validation) 