# Nearest Point Problem

Given a set of points in two-dimensional space, find and print the distance between the nearest points.

### Input

The input file contains several test cases. Each test case starts with an integer N (0 ≤ N ≤ 10000), which denotes the number of points in this set. The next N lines each contain two values that are the coordinates of the two-dimensional N points. The first of these two values indicates the X coordinate and the last one indicates the Y coordinate. The input is terminated by a set whose N = 0. This input should not be processed. The coordinate value will be a nonnegative number less than 40000. Example:

```python
3
0 0
10000 10000
20000 20000
5
0 2
6 67
43 71
39 107
189 140
0
```

### Output

For each input set printed, a single output line, including a floating point value (4 digits after the decimal point) or how far the two nearest points are. If these two points do not exist in the entry whose distance is less than 10000, print the message "INFINITY" without quotation marks.

```python
INFINITY
36.2215
```