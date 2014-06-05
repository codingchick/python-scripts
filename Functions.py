def take_user_input(num):
    input_value = raw_input("Please enter the " + num + " integer: ")

    while (input_value == '0' and num != 'first') or not input_value.isdigit():
        if input_value == '0':
            input_value = raw_input("Cannot divide by zero. Please enter the " + num + " integer: ")
        else:
            input_value = raw_input("Not valid integer. Please enter the " + num + " integer: ")

    input_value = int(input_value)

    return input_value

i1 = take_user_input('first')
i2 = take_user_input('second')

ints_sum = i1 + i2
ints_minus = i1 - i2
ints_multi = i1 * i2
ints_divide = i1 / i2
ints_remain = i1 % i2

print "The sum of " + str(i1) + " and " + str(i2) + " is: " + str(ints_sum)
print "The difference of " + str(i1) + " and " + str(i2) + " is: " + str(ints_minus)
print "The product of " + str(i1) + " and " + str(i2) + " is: " + str(ints_multi)
print "The quotient of " + str(i1) + " and " + str(i2) + " is: " + str(ints_divide) + " with a remainder: " + \
      str(ints_remain)

