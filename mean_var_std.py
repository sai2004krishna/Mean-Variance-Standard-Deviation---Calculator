import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    inputmatrix = np.array(list).reshape(3, 3)

    mean = [
        inputmatrix.mean(axis=0).tolist(),
        inputmatrix.mean(axis=1).tolist(),
        inputmatrix.mean().tolist()
    ]

    variance = [
        inputmatrix.var(axis=0).tolist(),
        inputmatrix.var(axis=1).tolist(),
        inputmatrix.var().tolist()
    ]

    std_dev = [
        inputmatrix.std(axis=0).tolist(),
        inputmatrix.std(axis=1).tolist(),
        inputmatrix.std().tolist()
    ]

    maximum = [
        inputmatrix.max(axis=0).tolist(),
        inputmatrix.max(axis=1).tolist(),
        inputmatrix.max().tolist()
    ]

    minimum = [
        inputmatrix.min(axis=0).tolist(),
        inputmatrix.min(axis=1).tolist(),
        inputmatrix.min().tolist()
    ]

    total_sum = [
        inputmatrix.sum(axis=0).tolist(),
        inputmatrix.sum(axis=1).tolist(),
        inputmatrix.sum().tolist()
    ]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': maximum,
        'min': minimum,
        'sum': total_sum
    }




    return calculations