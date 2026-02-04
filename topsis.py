import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    df = pd.read_csv(input_file)

    data = df.iloc[:, 1:].values
    weights = np.array(weights)
    impacts = np.array(impacts)

    # Step 1: Normalize
    norm = np.sqrt((data ** 2).sum(axis=0))
    normalized = data / norm

    # Step 2: Weighted normalized
    weighted = normalized * weights

    # Step 3: Ideal best & worst
    ideal_best = np.where(impacts == '+', weighted.max(axis=0), weighted.min(axis=0))
    ideal_worst = np.where(impacts == '+', weighted.min(axis=0), weighted.max(axis=0))

    # Step 4: Distances
    d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Score
    score = d_worst / (d_best + d_worst)
    rank = score.argsort()[::-1] + 1

    df['Topsis Score'] = score
    df['Rank'] = rank

    df.to_csv(output_file, index=False)
