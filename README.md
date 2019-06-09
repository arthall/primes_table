# Primes

## Running the program

This program requires Python 3. I tested it with Python 3.7.3.  It does not require any
additional packages to run.

To run the program with the default table size run prime_tables.py with no options.

    python3 primes_table.py

This will produce the following outout.

```
-------------------------------------------------------------------
|   * |   2 |   3 |   5 |   7 |  11 |  13 |  17 |  19 |  23 |  29 |
-------------------------------------------------------------------
|   2 |   4 |   6 |  10 |  14 |  22 |  26 |  34 |  38 |  46 |  58 |
-------------------------------------------------------------------
|   3 |   6 |   9 |  15 |  21 |  33 |  39 |  51 |  57 |  69 |  87 |
-------------------------------------------------------------------
|   5 |  10 |  15 |  25 |  35 |  55 |  65 |  85 |  95 | 115 | 145 |
-------------------------------------------------------------------
|   7 |  14 |  21 |  35 |  49 |  77 |  91 | 119 | 133 | 161 | 203 |
-------------------------------------------------------------------
|  11 |  22 |  33 |  55 |  77 | 121 | 143 | 187 | 209 | 253 | 319 |
-------------------------------------------------------------------
|  13 |  26 |  39 |  65 |  91 | 143 | 169 | 221 | 247 | 299 | 377 |
-------------------------------------------------------------------
|  17 |  34 |  51 |  85 | 119 | 187 | 221 | 289 | 323 | 391 | 493 |
-------------------------------------------------------------------
|  19 |  38 |  57 |  95 | 133 | 209 | 247 | 323 | 361 | 437 | 551 |
-------------------------------------------------------------------
|  23 |  46 |  69 | 115 | 161 | 253 | 299 | 391 | 437 | 529 | 667 |
-------------------------------------------------------------------
|  29 |  58 |  87 | 145 | 203 | 319 | 377 | 493 | 551 | 667 | 841 |
-------------------------------------------------------------------
```

The program can accept one parameter -t, --table_size which is an interger
value for the number of primes to include in the multiplication table.

The help can be displayed with -h, --help

```
$ python3 primes_table.py --help
usage: primes_table.py [-h] [-t TABLE_SIZE]

Generate a multiplication table of prime numbers

optional arguments:
  -h, --help            show this help message and exit
  -t TABLE_SIZE, --table_size TABLE_SIZE
                        The number of primes to use when generating the table.

```

## Testing, type checking and linting

Tests, type checking and linting require additional packages. Before installing
these packages it is a good idea to setup a virual environment for development. 
I recommend [pyenv](https://github.com/pyenv/pyenv), for setting up multiple versions
of Python and creating virtual environments.

Once you have your virtual environment setup, you can install the packages required
for testing, type checking and linting with pip.  The required extra packages are
Pytest, Pytest-cov, Flake8 and Mypy.  They also have dependencies which will be
installed.

To install the extra packages there is a requirements.txt file included.  Pip 
can use this file to install all of the packages at once.

    pip install -r requirements.txt

### Testing

Pytest is used to run the tests.  To run the default tests run pytest without any parameters.

```
$ pytest
================================== test session starts ===================================
platform linux -- Python 3.7.3, pytest-4.6.2, py-1.8.0, pluggy-0.12.0
rootdir: /home/art/Projects/Python/primes
plugins: cov-2.7.1
collected 7 items                                                                        

tests/test_multiplication_table.py ...                                             [ 42%]
tests/test_primes.py ..ss                                                          [100%]

========================== 5 passed, 2 skipped in 0.04 seconds ===========================
```

To run the all the tests, including the slow ones, use the --runslow flag.

    pytest --runslow

To see a coverage report for the tests, run the following.

    pytest --cov=primes

### Type checking

Mypy is used to perform static type checking. To verify the types run mypy with the --strict flag.

    mypy --strict *.py

### Linting

Flake8 is used to check the project for style issues and lint.  The only configuration change I made to
is to accept lines upto 120 characters rather than the default of 80.  The configuration is stored in .flake8.
This allows Flake8 to be run with no parameters.

    flake8
