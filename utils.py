class utils:
    """ A class that contains utility functions. """

    @staticmethod
    def reversed(n: int) -> int:
        """ Accepts an int and returns the number reveresed in int."""
        if not isinstance(n, int):
            try:
                n = int(n)
            except (ValueError, TypeError):
                raise TypeError("Input must be convertible to an integer.")

        if n < 0: # for negative numbers, we need to handle the sign separately
            return - int(str(-n)[::-1])

        return int(str(n)[::-1])

    @staticmethod
    def formatter(n: int) -> tuple[str, str]:
        """ Accepts an int and returns the number in base 2 (binary) and base 8 (octal) format. """
        if not isinstance(n, int):
            try:
                n = int(n)
            except (ValueError, TypeError):
                raise TypeError("Input must be convertible to an integer.")
            
        return bin(n), oct(n)