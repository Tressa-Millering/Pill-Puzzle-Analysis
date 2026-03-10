# sg1-pill-puzzle

## Authors

* Riddhi Acharya

* Zachary Gmyr

* Caleb Hackmann

* Tressa Millering

* Devon Schrader

## Project Motivation

The goal of this project was to collaboratively design, implement and test a software solution to the classic "[Pill Puzzle](https://en.wikipedia.org/wiki/Pill_puzzle)" probability problem. SG1 is a simulation-based (brute force) solution that uses visualization and statistical analysis to explore the results.

> This project was developed as a group assignment for CS 4500 – Introduction to the Software Profession at the University of Missouri–St. Louis (UMSL).

## Project Description

SG1 is an interactive Python 3 program designed to run in the Thonny IDE, but developed with PyCharm. The `NumPy` and `matplotlib` packages are required for visuals and statistical analysis.

The pill puzzle begins with **N whole pills** in a bottle. A patient must take **half a pill each day**, but the pills are initially whole. Each day a pill is randomly selected from the bottle:

* if a whole pill is selected → pill is split in half; one half is taken, the other returned to the bottle

* if a half pill is selected → pill is simply taken and removed from the bottle

Since each pill is eventually split in half, this process lasts exactly **2 \* N days**, ending with an empty bottle.

SG1 runs the simulation **R times** and aggregates the results to estimate statistical properties of the system.

After the simulations complete, the program allows the user to explore the results through an interactive menu which answers the following questions:

1. Expected number of whole and half pills remaining on a given day
2. Most likely day the bottle runs out of whole pills, and day the first half pill is taken
3. Average rate at which whole pills decrease over time

To help visualize these results, the program generates several plots using Matplotlib, including:

* A line graph showing the average number of whole and half pills remaining each day

- Histograms showing the frequency of when key events occur during simulations

- A regression plot showing the rate of decrease of whole pills over time

## Data Structures Used

SG1 primarily relies on NumPy arrays to store simulation results & perform calculations.

**Global Structures:**

`simulation_totals[day][2]` → 2-dimensional array used to accumulate the total number of whole & half pills for each day across all simulations

* each entry contains: `[whole_pills, half_pills]`

- The array contains 2 × N + 1 rows, representing days from 0 to 2 × N.

`simulation_averages[day][2]` → after all simulations complete, this 2-dimensional array stores the average number of whole & half pills per day.

* calculated with NumPy's element-wise division: `simulation_averages = simulation_totals / R`

- each element contains floating-point values representing the average pill counts

`last_whole_days[simulation]` → records the day each simulation runs out of whole pills

* each element stores an integer representing the day when the final whole pill was taken

`first_half_days[simulation]` → records the first day a half pill is selected in each simulation

* each element stores an integer representing the day this event occurred

## Compilation and Usage

#### Requirements

This program requires **Python 3.10** or later, and requires the following packages: `NumPy`, `Matplotlib`

If using Thonny IDE, packages can be installed at:

```
Tools → Manage Packages
```

Or using pip:

```
pip install numpy matplotlib
```

#### Running the Program

SG1 is designed to run in Thonny IDE

1. open `SG1.py` in Thonny
2. click the green Run button or press `f5`

To run from the command line, use:

```
python SG1.py
```

#### Workflow

When the program starts, the user will be prompted to enter:

```
N  → number of starting whole pills (1–1000)
R  → number of simulation repetitions (1–10000)
```

The program will then initialize simulation data structures,run the program displaying a progress bar, and present a Results Menu where the user can view graphs and statistical results.

> Graphs will open in a separate window using Matplotlib

The user can choose from the following questions to see an analysis:

```
1) Expected number of whole and half pills on a given day
2) Most likely day when whole pills run out and when the first half pill appears
3) Average rate that whole pills decrease over time
```
