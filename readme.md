Hamming Decoder
===============

This package provides the basic structure and tests for a [Hamming code](https://en.wikipedia.org/wiki/Hamming_code) decoder.

The implementation should be added to `hamming.py`.

Tests may be run by invoking either `make test` or `python3 -m doctest hamming.py`.

Once complete, the decoder can extract data from Hamming codes including 0 or 1 bit errors as follows:

```sh
> python3 hamming.py 111
1

> python3 hamming.py 110
1

> python3 hamming.py 1111111
1111

> python3 hamming.py 1111011
1111
```
