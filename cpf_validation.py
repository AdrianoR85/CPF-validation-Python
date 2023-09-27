print('Fomart valid: xxx.xxx.xxx-xx')
input_cpf = input('Enter with a CPF: ')
cpf_without_dot = ''.join(input_cpf[0:11].split('.'))
counter = 10

def sum_of_digits(cpf, counter):
  sum = 0
  for digit_str in cpf:
    sum += int(digit_str) * counter
    counter -=1
  return sum


def get_one_digit(result_sum_digits):
  new_digit = ''
  rest = (result_sum_digits * 10) % 11
  new_digit = str(0) if rest > 9 else str(rest)
    
  return new_digit
   

def format_cpf(cpf):
  new_cpf = ''
  for i in range(0, len(cpf)):
    if i == 3 or i == 6:
      new_cpf += '.'
    
    if i == 9:
      new_cpf += '-'
  
    new_cpf += cpf[i]  
  return new_cpf
  
  
result_of_sum = sum_of_digits(cpf_without_dot, counter)
first_digit = get_one_digit(result_of_sum)
cpf_without_dot += first_digit

counter += 1

result_of_sum = sum_of_digits(cpf_without_dot, counter)
second_digit = get_one_digit(result_of_sum)
cpf_without_dot += second_digit    

new_cpf = format_cpf(cpf_without_dot)

message = 'CPF is valid' if input_cpf == new_cpf else 'CPF is not valid'
print(message)