# Code2College
#
# Foobar File Example
#
# This version uses PrettyTable. It is available in PythonAnywhere already.
# For Windows Install it with: pip3 install PTable
# For Linux: sudo pip3 install PTable
# See http://zetcode.com/python/prettytable/

#################
# Imports
#################
from prettytable import PrettyTable

# Miscellaneous global variables go here.

x = PrettyTable()
x.field_names = ["Day", "Year", "foobar(day, year)"]  # Set up table headings for output


#################
# Input Test Cases
#################
# These tuples define input test cases to apply to the function.
# Uncomment one case to use at a time.

# Test 1 - Use 3 days and 3 years.
"""years = (2017, 2018, 2019)
days = ("Monday", "Tuesday", "Wednesday")
"""#

# Test 2 - Use all the days of the week and 4 years.
years = (2017, 2018,  2019, 2020)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# End of input test cases


#################
# Functions
#################


#################
# FUNCTION foobar
#
def foobar(_day, _year):
    r"""This function does something."""

    if not (_year == 2018) or (_day == "Tuesday"):
       msg = "Foo"
    else:
       msg = "Bar"

    return  msg # foobar
#################


#################
# Execution starts here
#################

# Open the file and erase any previous copy of it.
g = open('foobar_results.txt', 'w')

# Write an introduction heading to the file first.
g.write('Results saved in this file:\n')
g.close  # close the file.

#
# This code uses nested for loops that cycles through the days for each year and calls the foobar function.
#

# Open the file and append to add new content to the end.
g = open('foobar_results.txt', 'a')

for year in years:  # loop through the years - the outer loop
    for day in days:  # loop through the days - the inner loop
        x.add_row([day, year, foobar(day, year)])  # Add a row to the table
        #print(foobar(day, year))  # Print the raw output to the console
        g.write(foobar(day, year)) # Write raw output to the file not in a table.
# Close the file when finished with it!
g.write('\n')  # next line
g.close  # close the file.

# Write the whole table of results

# Write the table of results using with
with open('foobar_results.txt', 'a') as g:
    g.write(str(x))  # Write the table in x to the file.
# file is closed when we get here.


print("\n\nResults to the console:\n"); print(x)  # Print the table to console

print("Done.")
#g.close
