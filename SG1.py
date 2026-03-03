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
import matplotlib.pyplot as plt

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
#Displays a visual progress bar during simulation execution. 
#Called once per simulation inside run_simulations(). 
#Calculates percent completion and updates the same console line in-place. 
#Globals Used: None
def loading_screen(sim, R):
    bar_length = 30
    progress = sim / R
    filled = int(progress * bar_length)
    empty = bar_length - filled

    bar = "█" * filled + "░" * empty
    percent = int(progress * 100)

    print(f"\r[{bar}] {percent}%", end="")

#*******************************************
#Runs R simulations, outputting a loading screen as it goes
#Globals Used: R, simulation_totals, simulation_averages
def run_simulations():
    global simulation_averages
    print("\nRunning simulations...\n")

    for sim in range(0, R):
        single_simulation(sim)
        loading_screen(sim + 1, R)  # +1 ensures it reaches 100%

    simulation_averages = np.divide(simulation_totals, R)
    print("\nSimulations complete!\n")

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
    whole_total = N
    half_total = 0

    simulation_totals[0][0] += N   # Day 0: start with N whole pills

    for day in range(1, 2*N + 1):
        whole_probability = get_whole_probability(whole_total, half_total)
        pill_grab = np.random.random()
        if pill_grab < whole_probability:
            whole_total -= 1
            half_total += 1
            if whole_total == 0:
                last_whole_days[sim] = day
        else:
            half_total -= 1
            if not first_half_out:
                first_half_out = True
                first_half_days[sim] = day

        simulation_totals[day][0] += whole_total
        simulation_totals[day][1] += half_total


#*******************************************



#REMOVE THIS NOTE LATER
#This was Riddhi's function from statistics.py
#Tressa moved it here because we need to keep everything
#in the same file. Renamed stuff just because it can
#be used generically as a mode function

#*******************************************
#Calculates array mode
#Primarily used for last whole day and first
#half day calculation
def array_mode(array):
    flat_array = array.flatten()

    values, counts = np.unique(flat_array, return_counts=True)
    mode = values[np.argmax(counts)]

    return mode

#********************************************



#********************************************
#Prints min, mean, mode, and max of an array
#Used primarily for question 2
def array_stats(array):
    flat_array = array.flatten()
    print("\tEarliest Day:", np.min(array))
    print("\tAverage Day: ", np.mean(array))
    print("\tSmallest Mode Day: ", array_mode(array))
    print("\tLatest Day:  ", np.max(array))

#********************************************


#********************************************
#Output statistics related to question 2
#Globals Used: last_whole_days, first_half_days
def question2_stats():
    print("Question 2 statistics:\n-------------------------\n")
    print("LAST WHOLE DAY ANALYSIS\n")
    array_stats(last_whole_days)
    #Prompt y/n to see histogram of last whole

    print("\n\nFIRST HALF DAY ANALYSIS\n")
    array_stats(first_half_days)
    #Prompt y/n to see histogram of first half

#********************************************



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
# -------------------------
# Q1 FUNCTIONS
# -------------------------
def plot_q1_averages():
    days = np.arange(0, 2*N + 1)

    avg_whole = simulation_averages[:, 0]
    avg_half = simulation_averages[:, 1]

    plt.figure()
    plt.plot(days, avg_whole, label="Average Whole Pills")
    plt.plot(days, avg_half, label="Average Half Pills")

    plt.xlabel("Day")
    plt.ylabel("Average Pill Count")
    plt.title("Average Whole and Half Pills Per Day")
    plt.legend()
    plt.show()

def q1_console():
    while True:
        day = int(input("Enter a day (0 to {}), or -1 to return: ".format(2*N)))

        if day == -1:
            break

        if 0 <= day <= 2*N:
            print("Day", day)
            print("Average Whole Pills:", simulation_averages[day][0])
            print("Average Half Pills:", simulation_averages[day][1])
        else:
            print("Invalid day.")
# -------------------------
# Q2 FUNCTIONS
# -------------------------

def plot_q2_histograms():
    plt.figure()
    plt.hist(last_whole_days.flatten(), bins=20)
    plt.title("Histogram of Last Whole Pill Day")
    plt.xlabel("Day")
    plt.ylabel("Frequency")
    plt.show()

    plt.figure()
    plt.hist(first_half_days.flatten(), bins=20)
    plt.title("Histogram of First Half Pill Day")
    plt.xlabel("Day")
    plt.ylabel("Frequency")
    plt.show()

def q2_console():
    last_mode = array_mode(last_whole_days)
    first_mode = array_mode(first_half_days)

    print("Whole pills most often ran out on day:", last_mode)
    print("Half pills were most often first taken on day:", first_mode)

    input("Press ENTER to return...")

# -------------------------
# Q3 FUNCTIONS
# -------------------------

def plot_q3_regression():
    days = np.arange(0, 2*N + 1)
    avg_whole = simulation_averages[:, 0]

    # Scatter
    plt.figure()
    plt.scatter(days, avg_whole)

    # Line of best fit
    m, b = np.polyfit(days, avg_whole, 1)
    plt.plot(days, m*days + b)

    plt.xlabel("Day")
    plt.ylabel("Average Whole Pills")
    plt.title("Whole Pills Decrease Over Time")
    plt.show()

    print("Whole pills were taken at a rate of approximately",
          round(abs(m), 4), "pills per day.")
    input("Press ENTER to return...")

# -------------------------
# RESULTS MENU
# -------------------------
def results_menu():
    while True:
        print("\nResults Menu")
        print("1 - Q1 Averages")
        print("2 - Q2 Statistics")
        print("3 - Q3 Regression")
        print("0 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            plot_q1_averages()
            q1_console()
        elif choice == "2":
            plot_q2_histograms()
            q2_console()
        elif choice == "3":
            plot_q3_regression()
        elif choice == "0":
            break
        else:
            print("Invalid option.")


#*******************************************
#main (obviously)
def main():
    print("======== Welcome to the Pill Program! ========")
    print("This program will create a pill bottle with 'N' pills and simulate emptying it 'R' times!\n"
          "Statistics will be provided regarding the contents of the bottle for the simulation.\n")
    global N, R
    N = get_N()
    R = get_R()
    initialize_arrays()
    run_simulations()

    question2_stats()
    results_menu()

#*******************************************


if __name__ == "__main__":
    main()
