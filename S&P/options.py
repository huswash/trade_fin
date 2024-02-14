import numpy as np


def binomial_model(S, K, r, T, sigma, option_type, n):
    """
    S: initial stock price
    K: strike price
    r: risk-free interest rate
    T: time to maturity
    sigma: volatility
    option_type: 'call' or 'put'
    n: number of time steps
    """
    delta_t = T / n
    u = np.exp(sigma * np.sqrt(delta_t))
    d = 1 / u
    p = (np.exp(r * delta_t) - d) / (u - d)

    # create the binomial price tree
    price_tree = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(i + 1):
            price_tree[j, i] = S * (u ** (i - j)) * (d ** j)

    # create the option value tree
    option = np.zeros((n + 1, n + 1))
    if option_type == 'call':
        option[:, n] = np.maximum(np.zeros(n + 1), price_tree[:, n] - K)
    else:
        option[:, n] = np.maximum(np.zeros(n + 1), K - price_tree[:, n])

    # calculate option price at t=0
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            option[j, i] = np.exp(-r * delta_t) * (p * option[j, i + 1] + (1 - p) * option[j + 1, i + 1])

    return option[0, 0]

def binomial_call_full(S_ini, K, T, r, u, d, N):
    dt = T / N  # Time step
    p = (np.exp(r * dt) - d) / (u - d)  # Risk neutral probabilities (probs)
    C = np.zeros([N + 1, N + 1])  # Call prices
    S = np.zeros([N + 1, N + 1])  # Underlying price
    for i in range(0, N + 1):
        C[N, i] = max(S_ini * (u ** (i)) * (d ** (N - i)) - K, 0)
        S[N, i] = S_ini * (u ** (i)) * (d ** (N - i))
    for j in range(N - 1, -1, -1):
        for i in range(0, j + 1):
            C[j, i] = np.exp(-r * dt) * (p * C[j + 1, i + 1] + (1 - p) * C[j + 1, i])
            S[j, i] = S_ini * (u ** (i)) * (d ** (j - i))
    return C[0, 0], C, S

def binomial_put_full(S_ini, K, T, r, u, d, N):
    dt = T / N  # Define time step
    p = (np.exp(r * dt) - d) / (u - d)  # Risk neutral probs
    P = np.zeros([N + 1, N + 1])  # Call prices
    S = np.zeros([N + 1, N + 1])  # Underlying price
    for i in range(0, N + 1):
        P[N, i] = max(K - (S_ini * (u ** (i)) * (d ** (N - i))), 0)
        S[N, i] = S_ini * (u ** (i)) * (d ** (N - i))
    for j in range(N - 1, -1, -1):
        for i in range(0, j + 1):
            P[j, i] = np.exp(-r * dt) * (p * P[j + 1, i + 1] + (1 - p) * P[j + 1, i])
            S[j, i] = S_ini * (u ** (i)) * (d ** (j - i))
    return P[0, 0], P, S