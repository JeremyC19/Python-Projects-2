num_a = int(input('Enter first positive integer:\n'))
num_b = int(input('Enter second positive integer:\n'))

while num_a != num_b:
    if num_b > num_a:
        num_b = num_b - num_a
    else:
        num_a = num_a - num_b

print('GCD is %d' % num_a)

