#This is a comment. The hashtag at the beginning of the line tells
#the computer to ignore these lines. You must put a new hashtag
#for each line.

"""
For longer comments, put them inside triple quotes.
Everything inside the triple quotes will be ignored.
"""

"""
Your script should start with a comment that explains
what your script does:
This script converts a list of square foot measurements
to acres.
This script can be run from the command line. This file does 
not need to be open to run the script on the command line.
Run the script on the command line by navigating to the
folder that contains this script and
typing python acre_script.py.
"""

#if you have any modules to import, import them at the top of the script,
#under the comments

#assign any variables here
test_list = [5000, 6500, 8000, 15251]
factor = 43560

#include any function definitions here
def sqft_to_acres(sqft):
	#this function takes square footage and returns rounded acreage
	acres = sqft/factor
	return round(acres, 2)

#the rest of your code, including calling any functions, goes here
for test_value in test_list:
	answer = sqft_to_acres(test_value)
	print(str(test_value) + " square feet is " + str(answer) + " acres.")


        
