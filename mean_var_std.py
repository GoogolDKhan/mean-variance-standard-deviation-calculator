import numpy as np


def calculate(list):

    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")

    array = np.array(list)
    matrix = array.reshape((3, 3))

    mean_arr = [
        np.mean(matrix, axis=0).tolist(),
        np.mean(matrix, axis=1).tolist(),
        array.mean()
    ]
    var_arr = [
        np.var(matrix, axis=0).tolist(),
        np.var(matrix, axis=1).tolist(),
        array.var()
    ]
    std_arr = [
        np.std(matrix, axis=0).tolist(),
        np.std(matrix, axis=1).tolist(),
        array.std()
    ]
    max_arr = [
        np.max(matrix, axis=0).tolist(),
        np.max(matrix, axis=1).tolist(),
        array.max()
    ]
    min_arr = [
        np.min(matrix, axis=0).tolist(),
        np.min(matrix, axis=1).tolist(),
        array.min()
    ]
    sum_arr = [
        np.sum(matrix, axis=0).tolist(),
        np.sum(matrix, axis=1).tolist(),
        array.sum()
    ]

    return {
        'mean': mean_arr,
        'variance': var_arr,
        'standard deviation': std_arr,
        'max': max_arr,
        'min': min_arr,
        'sum': sum_arr
    }
