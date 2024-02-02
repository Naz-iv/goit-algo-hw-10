import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import quad


def plot_integral(func, a, b, n=1000):

    x = np.linspace(-0.5, 2.5, n)
    y = func(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2)

    ix = np.linspace(a, b)
    iy = func(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Integral of f(x) between {a} and {b}")
    plt.grid()
    plt.show()


def numeric_integral(func, a, b):
    result, error = quad(func, a, b)
    return result


def mc_integral(func, a, b, num_samples=10000):
    samples_x = np.random.uniform(a, b, num_samples)
    samples_y = np.random.uniform(0, func(b), num_samples)

    points_under_curve = sum(samples_y <= func(samples_x))

    area_ratio = points_under_curve / num_samples

    total_area = (b - a) * func(b)

    integral_value = total_area * area_ratio

    return integral_value


def main():

    def f(x):
        return x ** 2

    a = 0  # bottom range
    b = 2  # top range

    plot_integral(f, a, b)

    print(f"Numeric integral: {numeric_integral(f, a, b):.4f}")

    num_samples = (100, 1000, 10000, 100000, 1000000, 10000000)

    for sample in num_samples:
        print(f"Monte Carlo integral ({sample} samples): {mc_integral(f, a, b, num_samples=sample):.4f}")


if __name__ == "__main__":
    main()
