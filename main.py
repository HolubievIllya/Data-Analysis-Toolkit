def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def array_frequency(arr: list) -> dict:
    elements_count = {}
    for element in arr:
        if element in elements_count:
            elements_count[element] += 1
        else:
            elements_count[element] = 1
    return elements_count


def arithmetic_mean(arr: list) -> float:
    return sum(arr) / len(arr)


def harmonic_mean(arr: list) -> float:
    def obr(x):
        return 1 / x

    return len(arr) / sum(list(map(obr, arr)))


def mean_square(arr: list) -> float:
    def kvadr(x):
        return x * x

    return (sum(list(map(kvadr, arr))) / len(arr)) ** (1 / 2)


def geometric_mean(arr: list) -> float:
    geo_mean = 1
    for i in arr:
        geo_mean = geo_mean * (i ** (1 / len(arr)))
    return geo_mean


def mode(arr: list) -> list:
    counts = dict()
    for i in arr:
        counts[i] = counts.get(i, 0) + 1
    m = max(counts.values())
    return [i for i in list(counts.keys()) if counts[i] == m]


def median(arr: list) -> float | int:
    if len(arr) % 2 == 0:
        med = (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2) + 1]) / 2
    else:
        med = arr[int(len(arr) / 2 + 0.5)]
    return med


def range_of_variation(arr: list) -> float | int:
    return max(arr) - min(arr)


def mean_deviation(arr: list) -> float:
    def linear_function(nums):
        return abs(nums - sum(nums) / len(nums))

    return sum(list(map(linear_function, arr))) / len(arr)


def mean_squared_deviation(arr: list) -> float:
    def ser_kvadr(nums):
        return (nums - sum(nums) / len(nums)) ** 2

    return (sum(list(map(ser_kvadr, arr))) / len(arr)) ** 0.5


def dispersion(arr: list) -> float:
    def ser_kvadr(nums):
        return (nums - sum(nums) / len(nums)) ** 2

    return ((sum(list(map(ser_kvadr, arr))) / len(arr)) ** 0.5) ** 2


def coefficient_of_variation(arr: list) -> float:
    def ser_kvadr(nums):
        return (nums - sum(nums) / len(nums)) ** 2

    return (
        ((sum(list(map(ser_kvadr, arr))) / len(arr)) ** 0.5)
        / (sum(arr) / len(arr))
        * 100
    )


def coefficient_of_oscillation(arr: list) -> float:
    return max(arr) - min(arr) / sum(arr) / len(arr)


def covariance(data_x: list, data_y: list) -> float:
    mean_x = sum(data_x) / len(data_x)
    mean_y = sum(data_y) / len(data_y)
    sub_x = [i - mean_x for i in data_x]
    sub_y = [i - mean_y for i in data_y]
    return sum([sub_x[i] * sub_y[i] for i in range(len(sub_x))]) / (len(data_x) - 1)
