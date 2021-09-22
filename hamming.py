""" 
Accepts a string of hamming-encoded data and returns the data portion with any 1 bit
errors corrected.
"""


def parity_check(bits):
    """Returns true if `bits` has even parity

    >>> parity_check('')
    True

    >>> parity_check('11')
    True

    >>> parity_check('00')
    True

    >>> parity_check('01')
    False

    >>> parity_check('10')
    False

    >>> parity_check('10101010')
    True

    >>> parity_check('1010101010')
    False
    """


def get_error_position(hamming_code):
    """
    Returns 1-based position of an error in the supplied Hamming code

    Returns None if no error

    >>> get_error_position('111')

    >>> get_error_position('000')

    >>> get_error_position('110')
    3

    >>> get_error_position('100')
    1

    >>> get_error_position('1111111')

    >>> get_error_position('1110111')
    4

    >>> get_error_position('1111010')
    2
    """


def hamming_decode(bits):
    """
    Returns data portion of Hamming-coded bit string

    This function should support Hamming (3,1) and Hamming (7,4)

    >>> hamming_decode('111')
    '1'

    >>> hamming_decode('000')
    '0'

    >>> hamming_decode('001')
    '0'

    >>> hamming_decode('100')
    '0'

    >>> hamming_decode('110')
    '1'

    >>> hamming_decode('1111111')
    '1111'

    >>> hamming_decode('1110111')
    '1111'

    >>> hamming_decode('0111111')
    '1111'

    >>> hamming_decode('1111110')
    '1111'

    >>> hamming_decode('1011010')
    '1010'

    >>> hamming_decode('1111010')
    '1010'

    >>> hamming_decode('1001010')
    '1010'

    For 2 points of extra credit, you may also create a general implementation that
    allows the following tests to pass:

    >>> hamming_decode('011001001110001')
    '10101110001'

    >>> hamming_decode('011011001110001')
    '10101110001'

    >>> hamming_decode('001011111100111')
    '11111100111'

    >>> hamming_decode('001011111100110')
    '11111100111'

    >>> hamming_decode('1111111111111111111111111111111')
    '11111111111111111111111111'

    >>> hamming_decode('1111111111111111111111111111110')
    '11111111111111111111111111'

    >>> hamming_decode('1111111101111111111111111111111')
    '11111111111111111111111111'
    """


if __name__ == "__main__":
    import sys

    print(hamming_decode(sys.argv[1]))
