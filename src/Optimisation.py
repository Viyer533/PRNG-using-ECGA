import numpy as np
def entropy(X):
    
    alphabet = np.unique(X)
    frequency = np.zeros_like(alphabet)
    frequency = [np.sum(X == alphabet[symbol]) for symbol in range(len(alphabet))]
    P = frequency / np.sum(frequency)
    H = -np.sum(P * np.log2(P))
    UB = np.log2(len(alphabet))

    return H, UB

def seqperiod(W):
    periods = []
    n = len(W)

    for p in range(1, n + 1):
        if n % p == 0:
            is_periodic = all(W[i] == W[i % p] for i in range(n))
            if is_periodic:
                periods.append(p)

    return min(periods)

def optimisation(R_Decimal):
    W = R_Decimal

    i = 0
    while True:
        i+=1
        H_1, _ = entropy(W)
        P_1 = seqperiod(W)

        if abs(H_1 - 8) <= 0.05 and P_1 == len(W):
            break

        r_1 = np.random.permutation(len(W))[:256]
        P_e = np.random.permutation(256)[:256]
        P_e = P_e % 256
        W_crossover = W.copy()
        W_crossover[r_1] = P_e

        H_2, _ = entropy(W_crossover)
        P_2 = seqperiod(W_crossover)

        if P_2 >= P_1 and H_2 >= H_1:
            I_mutation = W_crossover
        else:
            I_mutation = W

        r_2 = np.random.permutation(len(W))[:2]
        W_mutation = I_mutation.copy()
        W_mutation[r_2[0]], W_mutation[r_2[1]] = W_mutation[r_2[1]], W_mutation[r_2[0]]

        if seqperiod(W_mutation) >= seqperiod(I_mutation):
            W_output = W_mutation
        else:
            W_output = I_mutation

        W = W_output

    R_Opt = W
    print(entropy(R_Decimal)[0],seqperiod(R_Decimal))
    print(entropy(R_Opt)[0],seqperiod(R_Opt))
    return R_Opt
