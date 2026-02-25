import numpy as np

def compute_most_likely_depletion_day(last_whole_days):
    # Flatten array since it's (R,1)
    flat_days = last_whole_days.flatten()

    values, counts = np.unique(flat_days, return_counts=True)
    most_likely_day = values[np.argmax(counts)]

    return most_likely_day