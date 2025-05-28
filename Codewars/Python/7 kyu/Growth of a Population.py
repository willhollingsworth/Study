"""Code wars.

for https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
"""


def nb_year(p0: int, percent: float, aug: int, p: int) -> int:
    pop = p0
    years = 0
    while pop < p:
        pop += int(pop * percent / 100) + aug
        years += 1
    return years


if __name__ == "__main__":
    print(nb_year(1500, 5, 100, 5000), 15)
    print(nb_year(1500000, 2.5, 10000, 2000000), 10)