import numpy as np

np.random.seed(42)
trials = 100000
rolls = np.random.randint(1, 7, size=trials)

empirical_prob_6 = np.mean(rolls == 6)

theoretical_prob_6 = 1/6

event_even = {x for x in rolls if x % 2 == 0}
event_high = {x for x in rolls if x >= 4}

print("P(even) =", len(event_even)/len(rolls))