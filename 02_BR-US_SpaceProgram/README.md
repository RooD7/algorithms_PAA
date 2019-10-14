# BR-US Space Program - Incomplete Solution

In the year 2027, the US-Brazil space program identified a new K3PTZ solar system where there is a suspicion that a life form based on unknown elements may exist. So far, Americans have led the program's advances by spearheading space engineering efforts, and now it's time for Brazilians to show value in genetic engineering.

Life always evolves into a more efficient form based on a genetic code composed of basic elements. Here on Earth, science says there are four bases: adenine, cytosine, guanine and thymine. Studying the electromagnetic waves captured from the K3PTZ system, Brazilian researchers identified three new viable alien bases to form life and named them X, E, P. They also found that for life to be viable in the K3PTZ system, it must host genomes formed. of stable single chains on the three alien bases. Each possible string is a sequence in the alphabet {X, E, P}. For a chain to be stable, it cannot have two adjacent equal subsequences. Develop a program to simulate experiments with new genomes, generating stable chains of certain lengths.

### Example:

The XEPXE chain is viable and sets up a genome. The XEPXPXE string is not viable because it has adjacent PX subsequences.

### Input

The input contains several test cases. Each test case is composed of an integer n. Assume that 1 ≤ n ≤ 5000. The last test case must be zero, that is, n = 0.

```python
1
2
10
20
0
```

### Output

For each test case specified by n print a line with any genome of length n. If no genome in length does not exist, print a blank line.

```python
X
XE
XEXPXEPXPE
XEXPXEPXPEXEPXEXPXEP
```