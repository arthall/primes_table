from primes.multiplication_table import MultiplicationTable


def test_build_table():
    """
    Verify the table is built correctly.
    """

    values = [1, 2, 3]
    mt = MultiplicationTable(values)
    assert len(mt.table) == len(values) + 1
    assert len(mt.table[0]) == len(values) + 1
    # The in the last column of the first row mulitplied by the value in the last row of the first column
    # should equal the value in the last row of the last column.
    assert int(mt.table[0][len(values)]) * int(mt.table[len(values)][0]) == int(mt.table[len(values)][len(values)])

    assert mt.table[0][0].strip() == '*'


def test_text_table_number_of_lines():
    """
    Verify the text table has the correct number of lines.
    """

    values = [2, 3]
    mt = MultiplicationTable(values)
    lines = mt._text_table()
    assert len(lines) == 7


def test_text_table_equal_lines():
    """
    Verify the line lengths in text table are all the same.
    """

    values = [5, 700]
    mt = MultiplicationTable(values)
    lines = mt._text_table()
    length = len(lines[0])

    for line in lines[1:]:
        assert length == len(line)
