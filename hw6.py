
def even_odd(num):
    if isinstance(num, int):
        return num % 2 == 0
    else:
        return None





def spelling(sentence):
    if sentence[0].isupper() and sentence[-1] == ".":
        return True
    else:
        return False



def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2
    else:
        return None



def closest_number(seq, target=0):
    closest = seq[0]
    for num in seq:
        if abs(num - target) < abs(closest - target):
            closest = num
    return closest




