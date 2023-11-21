def kahansum(xs):
    s, e = 0., 0.
    for x in xs:
        y = x + e
        temp = s
        s = temp + y
        e = (temp - s) + y
    return s


if __name__ == "__main__":
    import numpy as np

    xs = [0.7, 0.1, 0.3]
    print(sum(xs), np.sum(xs), kahansum(xs))
