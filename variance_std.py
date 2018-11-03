import numpy as np

# func for mean 
def find_mean(data):
    s = sum(data)
    N = len(data)
    mean = s / N
    return mean

a = [1,2,2,5,6]

# print(find_mean(a))

# func for data - mean

def find_diff(data):
    mean = find_mean(data)
    diff = []
    for num in data:
        diff.append(num-mean)
    return diff

print(find_diff(a))

# func for get variance

def find_variance(data):
    diff = find_diff(data)
    sq_diff = []
    for d in diff:
        sq_diff.append(d**2)
    sum_sq_diff = sum(sq_diff)
    variance = sum_sq_diff / len(data)
    return variance


# print(find_variance(a))

b=np.array([1.6,1.9,1.5,1.8,1.7])
# func get standard deviation

def find_std_deviaction(data):
    variance = find_variance(data)
    std_deviation = np.sqrt(variance)
    return std_deviation

print(find_std_deviaction(b))







