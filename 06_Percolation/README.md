# Percolation in the matrix - Incomplete Solution

Percolation problems are usually easy to state and difficult to solve. The term percolation is synonymous with leaching, which is the movement of fluid in the porous medium. A real example of percolation occurs when water percolates into the soil between rock fractures and cracks. Percolation models can be computationally modeled using graphs or matrices.

In graphs, the links that connect vertices are the edges of the graph. Each link receives a value of 1 or 0 denoting the open or closed state, respectively. If the link is open, the fluid passes through it, otherwise the propagation of the fluid does not happen on that link. Using the metaphor of the fluid in porous media, the fluid penetrates all open links in front of it, so to say that the vertices x and y are connected means that if we inject fluid under pressure at the vertex x the vertex y will get wet.

In matrices, the model is less intuitive but still quite simple to understand. In analogy to graphs, consider each cell in the matrix as a vertex connected to neighboring vertices by row or column movements. Thus, the matrix can be seen as the representation of a square graph in which every internal cell in the matrix is ​​represented by a vertex of degree 4. It is added that the matrix is ​​not circular, that is, column 1 is not connected. to column n, the same thing happens analogously to the rows. What makes this model less intuitive is that in it open or closed states are assigned to cells, that is, to vertices rather than edges. Thus, again using the metaphor of water propagating in the porous medium: when water arrives in a cell, if that cell is closed, water will not wet the cell and will not propagate through it; but if the cell is open, water will not only wet the cell but will pass through it to reach its neighboring cells. For example, if water gets to M [i, j] and the state of that cell is opened, then water will get wet M [i, j] and get to M [i+1, j], M [i-1, j], M [i, j+1], M [i, j-1] - obviously assuming in this case that iej are not matrix edge values.

### The Problem
Make an algorithm that, given as input a percolation matrix and a starting cell, wet all open cells in the matrix with as few "corrections" as possible in the matrix, each correction being understood as the change in the value of a cell, changing its value from closed (value 0) to open (value 1). Clarifying the statement further to avoid any doubt: (1) water will be continuously injected into the starting cell; (2) After water percolation stops, choose a closed cell and change its state to open; (3) return to step 2 until all open cells are wet; (4) print the cells that were corrected in the process.

Because this problem may take too long for generic entries, consider that the array size will always be small and almost all cells will be open.

### Input

The first line of input provides the maxlin and maxcol integers that define the size of the matrix. The second line provides the starting cell. The following lines provide the values of the percolation matrix cells.

### Input Example
```python
5, 5
(0, 4)
[ [1, 1, 1, 0, 1], [1, 1, 0, 0, 0], [1, 0, 1, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1] ]
```
### Output

A list of cells that have been corrected to allow water to wet all open cells.

### Output Example
```python
[(0, 3), (1, 4), (4, 2)]
```