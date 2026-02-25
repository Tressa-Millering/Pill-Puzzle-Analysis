#*************************************************************************************************
#   Language - Python 3.10
#   IDE - Primarily programmed using PyCharm for its
#         version control tools, later tested in Thonny
#
#   Authors -
#       - Riddhi Acharya
#       - Zachary Gmyr
#       - Caleb Hackmann
#       - Tressa Millering
#       - Devon Schrader
#
#   Important Dates -
#       Program started 02/2/2026
#       Program submitted 03/10/2026
#
#   Course -
#        CS 4500 - Intro to the Software Profession
#
#   Program Explanation -
#       TO DO
#
#   Outside Sources:   NOTE: apparently we have to include what we used it for
#                            "...and give at least a little information about what you found at each resource."
#                           So make sure to write that, even if its barely anything.
#
#       https://www.geeksforgeeks.org/python/global-keyword-in-python/
#           - Used to verify behaviour and usage of the global keyword
#       https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
#           - Used as reference on how to initialize arrays
#       https://numpy.org/doc/stable/reference/generated/numpy.divide.html
#           - Used as reference on how to divide numpy arrays more efficiently
#       https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
#           - Used as reference for numpy random function
#       https://docs.python.org/3/library/functions.html#int
#           - Used as reference on converting string input to int for integer verification (rejects float strings)
#       https://docs.python.org/3/tutorial/inputoutput.html
#           - Used for referencing formatted string literals
#       https://docs.python.org/3/tutorial/errors.html
#           - Used as reference for try-catch error exception in verify_input helper function

#*************************************************************************************************

import numpy as np

#********************************************
#Global variables/data structures

#Initialized with dummy values as they are global
#but unknown until runtime.

#ints
N = 0   #Pill count. 1 - 1k inclusive
R = 0   #Simulation count. 1 - 10k inclusive

#Arrays
simulation_totals = None    #Keeps a running total of whole pill and half pill counts per day
simulation_averages = None  #Stores the average whole/half pill total after finishing the simulations
last_whole_days = None      #Keeps track of each day that whole pills ran out
first_half_days = None      #Keeps track of each day that half pills were selected
#********************************************



#********************************************
#FOR DEBUGGING, WILL REMOVE BEFORE SUBMITTING

#print one of the arrays in a single line
#if you just do print(np array), each element is a new line
#this is just prettier for testing.
#Parameters: array is the array being printed
#            length is the number of elements to print (starting at 0)
#            label is an optional prefix for clarity in output
def print_array(array, length, label=""):
    print(label + (":" if (label != "") else ""))
    for _ in range(0, length):
        print(array[_], end=" ")
    print("\n")

#*******************************************



#*******************************************
#Called after getting user input for N and R.
#Iniitializes arrays with the proper size.
#Globals Used: N, R, simulation_totals, last_whole_days, first_half_days
def initialize_arrays():
    global simulation_totals, last_whole_days, first_half_days
    simulation_totals = np.array(np.zeros((2*N + 1, 2), dtype=int))
    last_whole_days = np.array(np.zeros((R,1), dtype=int))
    first_half_days = np.array(np.zeros((R,1), dtype=int))


#*******************************************



#*******************************************
#Runs R simulations, outputting a loading screen as it goes
#Globals Used: R, simulation_totals, simulation_averages
def run_simulations():
    global simulation_averages
    for sim in range(0, R):
        single_simulation(sim)
        #clear screen
        #loading screen
    simulation_averages = np.divide(simulation_totals, R)
    #maybe automatically show plot of averages here?
    print("Simulations complete!")

#*******************************************



#*******************************************
#Short helper function used for readability
#Returns probability of grabbing a whole pill
#Parameters are the number of whole and half pills
def get_whole_probability(whole_total, half_total):
    return whole_total/(whole_total + half_total)

#*******************************************


#*******************************************
#Run a single simulation of emptying the pill bottle.
#The parameter 'Sim' represents the current simulation being run
#Globals Used: N, simulation_totals, last_whole_days, first_half_days
def single_simulation(sim = 0):
    first_half_out = False
    last_whole_out = False
    whole_total = N
    half_total = 0

    simulation_totals[0][0] += N   # Day 0: start with N whole pills

    for day in range(1, 2*N + 1):
        whole_probability = get_whole_probability(whole_total, half_total)
        pill_grab = np.random.random()
        if pill_grab < whole_probability:
            whole_total -= 1
            half_total += 1
            if whole_total == 0 and not last_whole_out:
                last_whole_out = True
                last_whole_days[sim] = day
        else:
            half_total -= 1
            if half_total == 1 and not first_half_out:
                first_half_out = True
                first_half_days[sim] = day

        simulation_totals[day][0] += whole_total
        simulation_totals[day][1] += half_total


#*******************************************


# *******************************************
# Helper function used to read input for variables given a prompt & verifies the input is within bounds [1,upper_limit]
# Prompt must be provided from the caller (as used in get_N and get_R) & repeats if input is invalid
# Loops with explanation output if the input is not within bounds [1,upper_limit] or raised an error (non-integer)
# Returns the input value to caller if the above checks passed
def verify_input(prompt, upper_limit):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= upper_limit:
                return value
            else:
                print(f"Enter a number between 1 and {upper_limit}, try again.")
        except ValueError:
            print("Must enter a whole number, try again.")

# *******************************************


#*******************************************
# Prompts the user to provide a number of pills N to start the simulation with
# uses helper function verify_input with an appropriate prompt for N as well as an upper limit of 1000
def get_N():
    print("Provide a number of N whole pills to start the simulation with.")
    pills = verify_input("Enter N (1-1000): ", 1000)
    return pills

#*******************************************


# *******************************************
# Prompts the user to provide a number of repetitions R to run the simulation for
# uses helper function verify_input with an appropriate prompt for R as well as an upper limit of 10000
def get_R():
    print("Provide a number of R repetitions to run the simulation for.")
    repetitions = verify_input("Enter R (1-10000): ", 10000)
    return repetitions

# *******************************************


#*******************************************
#main (obviously)
def main():
    print("Main function")
    global N, R
    N = get_N()
    R = get_R()
    initialize_arrays()
    run_simulations()

#*******************************************


if __name__ == "__main__":
    main()