all: test

test: hamming.py
	python3 -m doctest hamming.py