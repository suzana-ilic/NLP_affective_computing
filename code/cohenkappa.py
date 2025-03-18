from sklearn.metrics import cohen_kappa_score
import numpy as np

# Annotator scores from example
scores_annotator_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
scores_annotator_2 = np.array([2, 2, 4, 4, 4, 6, 9, 1, 9])

# Compute Cohen's kappa score
kappa_score = cohen_kappa_score(scores_annotator_1, scores_annotator_2)
print(kappa_score)