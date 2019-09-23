# Skyline problem

A common classic problem in algorithms that handle drawing images is the elimination of hidden lines - lines obscured by other parts of the drawing. Develop a program in Python3 to help an architect draw a city skyline, given the location of buildings. To make the problem treatable, consider that all buildings have rectangular shapes and share a common base (the city in which they are built is very flat). The city is also viewed as two-dimensional. Each building will be specified by a triple order (Ei, Ai, Di), where Ei and Di are the left and right coordinates respectively of building i and Ai is the height of the building.

### Example:

The diagram below shows a graphical representation for an instance of the problem.

![alt text](https://github.com/RooD7/algorithms_PAA/images/01_1.png "Skyline Example")

The figure on the left graphically represents the input that will be provided verbatim. The figure on the right graphs the output that will also be provided verbatim.

### Input

The entrance is a sequence of triples of buildings. All building coordinates are integers less than 10,000 and there will be at least one and no more than 5000 buildings in the input file. The triples will be ordered by Ei, the x-coordinate to the left of the building, so that the building with the smallest x-coordinate on the left is the first in the input file. The triples will be provided one per line, ending the entry with the triple (0,0,0). Following is the entry for the example instance:

```python
(1.11.5)
(2,6,7)
(3.13.9)
(12,7,16)
(14,3,25)
(19,18,22)
(23.13,29)
(24,4,28)
(0,0,0)
```

### Output

The output consists of a sequence of integers (v1, v2, v3,.., Vn − 2, vn − 1, vn) that describe the horizon line, where each vi such that i is an odd number represents a coordinate x and each vi such that i is an even number represents a height. The sequence represents the "path" taken, for example, by the tip of a pen that begins by tapping the paper at the smallest x coordinate and then travels vertically and horizontally by tracing all the lines that define the skyline. Note that the last integer in the sequence defining the horizon line will always be a 0 (zero).

```python
(1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)
```