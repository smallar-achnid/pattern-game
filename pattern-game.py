#decide whether the pattern is arithmetic or geometric
import random

def assign_pattern_type():
	pattern_type_int = random.randrange(0,2)
	if pattern_type_int == 0:
		pattern_type = "arithmetic"
	else:
		pattern_type = "geometric"
	return pattern_type

#decide what number to start with
def assign_starting_number(pattern_type):
	#pattern_type = assign_pattern_type()
	if pattern_type == "arithmetic":
		starting_number = random.randrange(0,11)
	else:
		starting_number = random.randrange(1,6)
	print (pattern_type)
	return starting_number

#decide the increment
def assign_increment(pattern_type):
	#pattern_type = assign_pattern_type()
	if pattern_type == "arithmetic":
		increment = random.randrange(1,16)
	else:
		increment = random.randrange(1,6)
	print(pattern_type)
	return increment

#create a loop that starts with the starting number, increments 5 times, and displays the first 5 numbers

def create_pattern():
	pattern_type = assign_pattern_type()
	element = assign_starting_number(pattern_type)
	increment = assign_increment(pattern_type)
	pattern_list = [element]
	for i in range(5):
		if pattern_type == "arithmetic":
			element = element + increment
			pattern_list.append(element)
		else:
			element = element * increment
			pattern_list.append(element)
		print (element)
	return pattern_list

def display_pattern(pattern_list):
	#pattern_list = create_pattern()
	displayable_list = []
	for i in range(5):
		element = pattern_list[i]
		displayable_list.append(element)
	return displayable_list

#print(display_pattern())

#accept input for 6th number
def compare_user_input():
	pattern_list = create_pattern()
	displayable_list = display_pattern(pattern_list)
	print(displayable_list)
	correct_answer = False
	
	while correct_answer == False:
		user_answer = input("Enter your answer:")
		if int(user_answer) == pattern_list[5]:
			correct_answer = True
			start_over = input ("Correct! Would you like to play another level?")
		#else:
		#try_again = input ("Sorry, that's incorrect. Would you like to try again? Enter 'yes' or 'no'")
		#if try_again == 'yes':

			

	
print(compare_user_input())

#if the input is the same as the 6th number display "Correct"
	#allow option to start the next level or quit
	#if they quit, quit
	#if they start the next level start the steps over
	#update database: streak += 1
	#update database: score += 5

#if the input is not the same as the 6th number, display "Incorrect"
	#allow 3 options: try again, see answer, quit
	#if they quit, quit
	#if they say try again, display the same pattern as before
	#if they say see answer, display the same pattern as before with the sixth slot filled in
	#update database: streak = 0
