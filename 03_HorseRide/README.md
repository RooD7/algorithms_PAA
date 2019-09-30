# Shortest horse ride

This problem is a more interesting variant of the classic horse ride problem going through every square of a chess board without repetition. The present problem consists of, given a set of houses provided as input, determining the shortest path a horse can make to pass over all given houses, whether or not passing over any house at all.

An elegant way to model this problem is to map the horse's possible jumps in a 64-vertex graph where each vertex corresponds to a square of the board, as shown in the figure below:

![alt text](https://github.com/RooD7/algorithms_PAA/blob/master/images/01_1.png "Horse Ride Example")

The algorithms that solve this problem are not very efficient, so the input provided will be less than or equal to 15.

### Input

The entrance is a list of houses the horse should walk through. The starting house will be the first house on the list, then the horse can walk through them in any order to build the shortest possible route through all the houses. Following is the entry for the example instance:

```python
[ 1, 2, 57, 12, 5, 56 ]
```

### Output

The exit consists of an integer representing the number of horse jumps and on the next line the horse's route to the ride. Following is the output for the example instance:

```python
13
[1, 11, 17, 2, 12, 22, 5, 22, 39, 56, 46, 36, 42, 57]
```