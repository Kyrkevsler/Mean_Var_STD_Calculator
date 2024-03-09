from mean_var_std import calculate

# Test the function
print("--------------------------------------------------------------")
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = calculate(input_list)
print(output)
print("--------------------------------------------------------------")


# Test for ValueErrors
print("--------------------------------------------------------------")
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = calculate(input_list)
print(output)
print("--------------------------------------------------------------")