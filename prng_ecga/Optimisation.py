import numpy as np
from typing import Tuple


def entropy(input_seq: np.ndarray) -> Tuple[float, float]:
    alphabet = np.unique(input_seq)
    frequency = np.zeros_like(alphabet)
    frequency = [np.sum(input_seq == alphabet[symbol]) for symbol in range(len(alphabet))]
    probability = frequency / np.sum(frequency)
    entropy_value = -np.sum(probability * np.log2(probability))
    upper_bound = np.log2(len(alphabet))

    return entropy_value, upper_bound


def seqperiod(i_prns: np.ndarray) -> int:
    periods = []
    n = len(i_prns)

    for p in range(1, n + 1):
        if n % p == 0:
            is_periodic = all(i_prns[i] == i_prns[i % p] for i in range(n))
            if is_periodic:
                periods.append(p)

    return min(periods)


def optimisation(i_prns: np.ndarray) -> np.ndarray:
    iters = 0
    while True:
        iters += 1
        initial_entropy, _ = entropy(i_prns)
        intial_period = seqperiod(i_prns)

        if abs(initial_entropy - 8) <= 0.05 and intial_period == len(i_prns):
            break

        rand_indices = np.random.permutation(len(i_prns))[:256]
        rand_selection = np.random.permutation(256)[:256]
        cross_prns = i_prns.copy()
        cross_prns[rand_indices] = rand_selection

        cross_entropy, _ = entropy(cross_prns)
        cross_period = seqperiod(cross_prns)

        if cross_period >= intial_period and cross_entropy >= initial_entropy:
            temp_mutation = cross_prns
        else:
            temp_mutation = i_prns

        rand_swap_indices = np.random.permutation(len(i_prns))[:2]
        mutation_prns = temp_mutation.copy()
        mutation_prns[rand_swap_indices[0]], mutation_prns[rand_swap_indices[1]] = (
            mutation_prns[rand_swap_indices[1]],
            mutation_prns[rand_swap_indices[0]],
        )

        if seqperiod(mutation_prns) >= seqperiod(temp_mutation):
            prns_output = mutation_prns
        else:
            prns_output = temp_mutation

        i_prns = prns_output

    return i_prns
