all: test

test: hamming.py
	python3 -m doctest hamming.py

clean:
	rm -rf .mypycache __pycache__
