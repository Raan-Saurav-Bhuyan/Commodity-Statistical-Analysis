import numpy as np

def select_rank(trace_stat, trace_crit, alpha_index=1):
    """
    Select cointegration rank based on trace test.

    alpha_index:
    0 → 90%
    1 → 95%
    2 → 99%
    """

    rank = 0

    for i in range(len(trace_stat)):
        if trace_stat[i] > trace_crit[i][alpha_index]:
            rank += 1

    return rank
