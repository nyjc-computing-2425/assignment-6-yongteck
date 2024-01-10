In this assignment, you should write your code in a **readable** way.

Your function definitions should have **appropriate docstrings**.

# Assignment 6: Loops

# Part 1

Write a function, `clock(n)`, that will show the time and update it once every second, for `n` number of seconds.

Your clock should show the time in `HH:MM:SS` format without milliseconds.

**Hint:** Refer to the [Python documentation](https://docs.python.org/3.6/library/datetime.html#datetime-objects) on the `datetime` object to see how to get the parts of the time from it.

### Expected output

    >>> clock(3)
    12:59:17

# Part 2: Lowest common multiple (LCM)

A simple algorithm for calculating the lowest common multiple of integers `a` and `b` is as follows:

1. Check if `a` and `b` are equal
2. If they are equal, `a == b == lcm` (lowest common multiple) [EXIT]
3. If they are not equal, check whether `a` or `b` is smaller.
4. The smaller variable is incremented by its original value.
    - i.e. `a += a_original`, or `b += b_original`
5. Go back to Step 1

Implement the above algorithm using a `while` loop. Write your code as a function, `lcm(a, b)` that returns the lowest common multiple of `a` and `b`.

### Example output

    >>> lcm(2, 3)
    6
    >>> lcm(12, 5)
    60

# Part 3: Greatest common factor (GCF)

[Euclid's Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) is an algorithm for calculating the greatest common factor `g` of `a` and `b` such that both `a` and `b` are divisible by `g`:

1. Check if `a` and `b` are equal
2. If they are equal, `a == b == g` (greatest common factor) [EXIT]
3. If they are not equal, the difference between the two variables, `d`, must also be divisible by `g`: calculate the GCF of the two smallest variables among `a`, `b`, and `d` (Start from Step 1)

Implement the above algorithm using a `while` loop. Write your code as a function, `gcf(a, b)` that returns the greatest common factor of `a` and `b`.

### Example output

    >>> gcf(60, 48)
    12
    >>> gcf(70, 14)
    14

# Submission

Before submission, run the tests on your functions.
