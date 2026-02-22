
# Greetings
print("Feel free to add some more code below this print to make sure your IDE is set up properly\n"
        "  - commit with a message\n"
        "  - push to the repository\n"
        "  - check the repository to see your changes were pushed properly\n")

# Add stuff here:

print("Riddhi was here. PyCharm setup complete 🚀")

print("Tressa was here. Hope it pushes!")




# Pandas / NumPy / matplotlib demo for dice rolls
#   - NumPy: high-performance arrays, array computation & random number generation (used by Pandas)
#   - matplotlib: Python plotting library for data visualization (used by Pandas)
#   - Pandas: read CSVs, data manipulation, statistical analysis & machine learning

# Step 1: install packages in the terminal (Ctrl+`):
# >      pip install pandas numpy matplotlib

# Step 2: import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 3: generate 20 random 6-sided dice rolls
diceRolls = np.random.randint(1, 7, size=20) # 1 to 6 inclusive

# Step 4: use matplotlib to plot a histogram
plt.hist(diceRolls, bins=np.arange(1,8)-0.5, edgecolor='black') # create histogram with data arranged in bins 1-6
        # np.arange(1,8)-0.5 → [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5] (defines edge of bins to divide data into)
plt.xticks(range(1, 7))     # show integers 1-6 on x-axis

plt.xlabel("Dice Face")     # label axis
plt.ylabel("Frequency")
plt.title("Histogram of 20 Dice Rolls")   # title graph

plt.show() # display results

# Step 5: calculating min/max/avg
min_roll = np.min(diceRolls)
max_roll = np.max(diceRolls)
avg_roll = np.mean(diceRolls)

print("\nDice Rolls:", diceRolls)
print("Minimum:", min_roll)
print("Maximum:", max_roll)
print("Average:", avg_roll)
