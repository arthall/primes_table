import pytest
from primes.primes_generator import prime_generator


def test_first_ten():
    """
    Verify the first and last values of first 10 primes.
    """

    limit = 10
    first_ten_primes = list(prime_generator(limit))

    assert len(first_ten_primes) == limit
    assert first_ten_primes[0] == 2
    assert first_ten_primes[-1] == 29


def test_negative_value():
    """
    Verify that passing a negative number to the generator raises an error.
    """

    with pytest.raises(ValueError):
        list(prime_generator(-1))


@pytest.mark.slow
def test_generator():
    """
    Verify the 10,001th prime.  This test is based on Project Euler question 7.
    """

    primes = prime_generator(10001)

    answer = list(primes)[-1]

    assert answer == 104743


@pytest.mark.slow
def test_first_prime_over_one_million():
    """
    Verify all the prime numbers under 1,000,000 can be generated.
    """

    finished = False
    # Pick a sufficiently large number that the generator doesn't hit the limit
    primes = prime_generator(1000000)
    count = 0
    while True:
        prime = next(primes)
        count += 1
        if prime > 1000000:
            assert prime == 1000003
            finished = True
            break

    assert finished
    assert count == 78499
