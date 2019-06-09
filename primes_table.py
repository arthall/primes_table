import argparse

from primes_generator import prime_generator
from multiplication_table import MultiplicationTable

"""
This program will generate a mulitplication table of prime numers.
The default is to print a table of the first 10 primes.
"""


def get_table_size() -> int:
    """
    Parse the inputs to the program and return the table_size.

    :return: Value of the command line parameter
    :rtype: int
    """

    parser = argparse.ArgumentParser(description="Generate a multiplication table of prime numbers")
    parser.add_argument("-t", "--table_size",
                        help="The number of primes to use when generating the table.",
                        default=10,
                        type=int)

    return(int(parser.parse_args().table_size))


"""
If this program is run from the command line the command line parameters will be parsed and
the program will print a multiplication table.  If the program is imported, this section will
not run.
"""
if __name__ == "__main__":
    table_size = get_table_size()

    primes = list(prime_generator(table_size))

    table = MultiplicationTable(primes)
    table.print_table()
