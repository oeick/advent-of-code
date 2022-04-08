from timeit import default_timer as timer
import main


def measure(filename: str) -> (int, int):
    with open(filename, 'r') as fp:
        banks = [int(n) for n in fp.read().split()]
    t_0 = timer()
    main.solve(banks)
    t_1 = timer()
    return t_1 - t_0


if __name__ == '__main__':
    print('{:.3f} seconds'.format(measure('../input.txt')))
