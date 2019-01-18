# PROJECT: Perceptron as AND operator
# PROGRAMMER: Carlos Mertens - Udacity Student
#				Udacity Instructors (Machin Learning Engineer Nanodegree)
# DATE CREATED: (DD/MM/YY) 10/01/2019
# REVISED DATE: (DD/MM/YY)
# PURPOSE: To find the weights and bias for the AND perceptron.
#			Users set the weights and bias to be tested
# USAGE: ...

import pandas as pd

# Get input from user
weight1 = float(input("Provide the first weight: "))
weight2 = float(input("Provide the second weight: "))
bias = float(input("Provide the bias: "))

# Set the inputs and outputs for the AND perceptron
train_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
train_outputs = [False, False, False, True]
final_outputs = []
# NOTE: For OR Perceptron use: train_outputs = [False, True, True, True]
# For NOT perceptron use: train_outputs = [True, False, True, False]

# Train and test outputs
for train_input, train_output in zip(train_inputs, train_outputs):
	linear_combination = weight1 * train_input[0] + weight2 * train_input[1] + \
						 bias
	output = int(linear_combination >= 0)
	if output == train_output:
		is_correct = "Yes"
	else:
		is_correct = "No"
	final_outputs.append([train_input[0], train_input[1], linear_combination,
						  output, is_correct])

# Print results
num_wrong = len([output[4] for output in final_outputs if output[4] == 'No'])
output_frame = pd.DataFrame(final_outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))
