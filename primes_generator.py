import sys
from typing import Iterator


def prime_generator(limit: int = 10) -> Iterator[int]:
    """
    Generator for prime numbers

    The generator will stop at sys.maxsize reguardless of the limit

    note:: This will most likely run out of memory if too many primes are
           requested. I only tested it for primes up to 1,000,003.

    :param limit: Number of primes to generate.
    :type limit: Integers greater than 1

    :return: Generator that produces prime numbers in increasing value.
    :rtype: Iterator[int]
    """
    stop = sys.maxsize

    if limit < 1:
        raise ValueError("Limit must be greater than 0, {} passed in".format(limit))

    # 2 is the only even prime.
    primes = [2]
    yield(2)

    # Only need to check odd numbers.
    for i in range(3, stop, 2):
        if len(primes) >= limit:
            break
        prime = True
        largest_possible_divisor = (i / 3) + 1
        # Check if i is divisible by a known prime, skip the first prime, 2.
        for y in primes[1:]:
            if y < largest_possible_divisor:
                if i % y == 0:
                    prime = False
                    break
            else:
                break

        if prime:
            primes.append(i)
            yield(i)
