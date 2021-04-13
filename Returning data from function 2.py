def digit_sum_and_square_it(x):
    sum = 0
    for each in str(x):
        sum+=int(each)
    return sum

x = int(input("Enter x: "))
print("Addition of digit in x: ",digit_sum_and_square_it(x))
print("Then addition square is ",digit_sum_and_square_it(x)**2)