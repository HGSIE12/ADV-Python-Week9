import numpy as np

# 1) Implement stable softmax
def softmax_stable(scores):
    scores = scores - np.max(scores)   # stability trick
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores)
    return probs

# 2) Apply to score vector
scores = np.array([1.0, 2.0, 3.0])
probs = softmax_stable(scores)

# 3) Show probabilities and their sum
print("Probs:", probs)
print("Sum:", probs.sum())