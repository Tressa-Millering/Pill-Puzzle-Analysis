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
#       SG1.py runs a number of 'R' simulations to emulate the "Pill Puzzle" problem for a bottle of 'N' whole pills.
#       The user is prompted to enter values for 'N' and 'R', & each simulation empties the bottle obeying these rules:
#           1. selecting a half or whole pill from the bottle is decided randomly based on the bottle's contents that day
#           2. if a half pill is selected it is removed from the bottle to be taken
#           3. if a whole pill is selected it gets split in half, one half is taken and the other returned to the bottle
#
#       Every simulation should run for 2*N days, starting with 'N' whole pills on day 0 and no pills on day 2*N. A
#       simple counter is used for both whole & half pills in a given simulation, and the pill is selected randomly
#       each day using NumPy's 'random.random()' function.
#
#       A two-dimensional array (simulation_totals) is used to track the total number of whole & half pills each day
#       accumulated across all repetitions of the simulation.
#
#           (Data structure) simulation_totals[day][2]: { [whole, half], ... '2*N' entries }
#               > 'whole' and 'half' are integer values for # whole/half pills that day (index)
#
#       After all simulations are run, we calculate the average whole/half pills across each day using NumPy division to
#       divide simulation_totals element-wise (broadcasting) by the number of simulations ran (R), and store the resulting
#       data in an equivalent sized array (simulation_averages).
#
#           (Data structure) simulation_averages[day][2]: { [avgWhole, avgHalf], ... '2*N' entries }
#               > 'whole' and 'half' are float values for average # whole/half pills that day (index)
#
#       Two other arrays are used to track (1) the first day the bottle ran out of whole pills, and (2) the first day
#       a half pill was selected. These conditions are checked for each day in every simulation ran, and stored
#       appropriately in the arrays 'last_whole_days' & 'first_whole_days' per simulations 1 through R.
#
#           (Data structure) last_whole_days[simulation]: { sim_1, sim_2, ... 'R' entries }
#               > each element (sim_1, sim_2, etc.) is an integer value representing a day #
#               > each index represents a separate simulation ran
#
#           (Data structure) first_whole_days[simulation]: { sim_1, sim_2, ... 'R' entries }
#               > an element (sim_1, sim_2, etc.) is an integer value representing a day #
#               > each index represents a separate simulation ran
#
#       The data from these arrays are used to answer the following questions, provided to the user through an interactive
#       menu prompt that allows them see both calculations and visual data provided with NumPy & Matplotlib:
#           1. What are the expected number of whole & half pills on a given day?
#           2. Which day is most likely we run out of whole & half pills on a given day?
#           3. At what average rate were whole pills taken per day?
#
#       Visual data generated with Matplotlib for each of these questions include:
#           > Q1: plot of average whole & half pills each per day
#           > Q2: histograms showing frequencies of the day (1) the first half pill & (2) last whole pill taken for each simulation
#           > Q3: plot showing the decrease of whole pills over time with line of best fit describing rate of reduction
#
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
#       https://www.geeksforgeeks.org/python/triple-quotes-in-python/
#           - Used for formatting large prompts

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

    print(f"\r{bar}] {percent}%", end="")

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
# Helper function used to read input for variables given a prompt & verifies the input is within bounds provided.
# Prompt must be provided from the caller (as used in get_N and get_R) & reprinted if input is invalid
# Loops & outputs a usage message if the input is not within bounds [lower_limit,upper_limit] or raised an error (non-integer)
# Returns the input value to caller if the above checks passed
def verify_input(prompt, upper_limit, allow_exit=False):
    while True:
        try:
            user_input = input(prompt)

            if allow_exit and user_input == "":
                return ""

            if '.' in user_input:
                print("Input must not be a decimal, try again.")
                continue
            value = int(user_input)
            if 1 <= value <= upper_limit:
                return value
            else:
                print(f"Input must be between 1 and {upper_limit}, try again.")
        except ValueError:
            print("Input must be numeric, try again.")
# *******************************************



#*******************************************
# Prompts the user to provide a number of pills N to start the simulation with
# uses helper function verify_input with an appropriate prompt for N as well as an upper limit of 1000
def get_N():
    print("Provide a number of N whole pills to start the simulation with.")
    pills = verify_input("Enter N (1 .. 1000): ", 1000)
    return pills

#*******************************************



# *******************************************
# Prompts the user to provide a number of repetitions R to run the simulation for
# uses helper function verify_input with an appropriate prompt for R as well as an upper limit of 10000
def get_R():
    print("Provide a number of R repetitions to run the simulation for.")
    repetitions = verify_input("Enter R (1 .. 10000): ",10000)
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
    # opening prompt for Q1
    print(f"Each simulation started with {N} whole pills on day 0 and lasted {2*N} days. To see results for average"
          f"\n half/whole pills on a given day, follow the prompt below. Press 'ENTER' to return to the results menu.\n")

    # loop until user presses enter to exit
    while True:
        # prompt user for a day between 0 and 2*N, press 'ENTER' to exit
        day_prompt = f"Enter a Day (1..{2*N}), or press 'ENTER' (leave blank) to return: "
        day = verify_input(day_prompt, 2*N, True)

        match day:
            case "":
                # return user to results menu
                break
            case _:
                # day chosen was between 0..2*N
                print(f"\nDay {day} Average Pill Count:\n"
                      f"   > Whole Pills = {simulation_averages[day][0]}\n"
                      f"   > Half Pills = {simulation_averages[day][1]}\n")

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
    # loop until user presses enter to exit
    while True:
        # opening prompt
        print("""====================== Results Menu ======================
Select a question below (1..3) to see the simulation's results:
  1.) What are the expected number of whole & half pills on a given day?
  2.) Which day is most likely we run out of whole pills & which day is most likely the first half pill is taken?
  3.) At what average rate were whole pills taken per day?
  Or press 'ENTER' to exit (leave blank)\n""")

        # get input using verify_input helper with prompt for options 0..3
        choice = verify_input("Enter an option (1..3): ",3, True)

        # select appropriate helper to display results
        match choice:
            case "":
                break  # exit menu loop
            case 1:
                # alert user a graph was generated
                print("\n > Graph Generated: \"Average Whole and Half Pills Per Day\"\n"
                      "   This graph displays the average number of whole & half pills remaining for each day across all"
                        " simulations.\n   [KEY] X-axis: Day, Y-axis: Average Pill Count\n")

                plot_q1_averages()  # generate graph
                q1_console()    # prompt user for day-specific results
            case 2:
                # alert user 2 graphs were generated
                print("\n > Graph Generated: \"Histogram of First Half Pill Day\"\n"
                      "   This graph displays the frequencies of the first day a half pill was taken for each simulation\n"
                      "   [KEY] X-axis: Day, Y-axis: Frequency")
                print("\n > Graph Generated: \"Histogram of Last Whole Pill Day\"\n"
                      "   This graph displays the frequencies of the last day a whole pill was taken in each simulation\n"
                      "   [KEY] X-axis: Day, Y-axis: Frequency\n")

                plot_q2_histograms() # generate graphs
                q2_console()  # print results to console
            case 3:
                # alert user a graph was generated
                print("\n > Graph Generated: \"Whole Pills Decrease Over Time\"\n"
                      "   This graph displays the average number of whole pills remaining per day across all simulations\n"
                      "     with a line of best fit that displays the rate of reduction\n"
                      "   [KEY] X-axis: Day, Y-axis: Avg # Whole Pills Left\n")

                plot_q3_regression() # generate graph & print rate


#*******************************************
#main (obviously)
def main():
    print("======== Welcome to the Pill Program! ========")
    print("""This program will create a pill bottle containing 'N' pills and simulate emptying it 'R' times!
    
Our physician has told us to take half a pill each day but gave us a bottle of 'N' whole pills. The simulation begins
with these 'N' whole pills on day 0, and over the course of 2*N days we randomly select either a whole or half pill,
depending on what is left in the bottle; if a whole pill is selected it must must be split in half as per our recommended
dose, and the other half should be returned. On the last day our bottle will be empty.

After running the simulation a number of times (R), statistics will be provided regarding the bottle's contents in order
to answer the following questions:
    1. What are the expected number of whole & half pills on a given day?
    2. Which day is most likely we run out of whole pills & which day is most likely the first half pill is taken?
    3. At what average rate were whole pills taken per day?

Follow the prompts to begin the simulation. Results to the above questions may be selected from at the end.\n""")
    global N, R
    N = get_N()
    R = get_R()
    initialize_arrays()
    run_simulations()

    # question2_stats()   # merge this to q2_console()?
    results_menu()

#*******************************************


if __name__ == "__main__":
    main()