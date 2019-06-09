from typing import List


class MultiplicationTable:
    """
    MultiplicationTable

    Converts a list of integers into a multiplication table.
    """

    def __init__(self, values: List[int]):
        """
        Initialize the class and build the multiplication table.

        :param values: List values to convert into a multiplication table
        :type values: List of ints
        """

        self.values = values
        self.table = self._build_table()

    def _build_table(self) -> List[List[str]]:
        """
        Build the multiplication table.
        Each row consists a list of string values and table is a list of rows.

        :return: 
        :rtype: List of List of Str
        """

        table = []

        # first row
        row = [str(x) for x in self.values]
        row.insert(0, "*")
        table.append(row)

        # all other rows
        for y in self.values:
            row = [str(y * x) for x in self.values]
            row.insert(0, str(y))
            table.append(row)

        return table

    def _text_table(self) -> List[str]:
        """
        Build a text version of the table, ready for printing to a display or inserting into a text file.

        :return: The text version of the table.
        :rtype: List of str
        """

        separator = "|"
        horizontal = "-"

        rows = len(self.table)
        cols = len(self.table[rows - 1])

        # Get the largest value from the table to determine padding.
        largest_value = self.table[rows - 1][cols - 1]
        # Padding is the length of largest number value + 2 spaces, one before and after the value
        padding = len(largest_value) + 2

        row_length = len(separator) + cols * (padding + len(separator))
        row_separator = horizontal * row_length

        lines = []
        # Top of table
        lines.append(row_separator)
        for row in self.table:
            # Rows
            lines.append("{edge}{row}{edge}".format(edge=separator,
                                                    row=separator.join([x.rjust(padding - 1) + " " for x in row])))
            lines.append(row_separator)

        return lines

    def print_table(self) -> None:
        """
        Print the multiplication table to standard out
        """

        lines = self._text_table()

        for line in lines:
            print(line)
