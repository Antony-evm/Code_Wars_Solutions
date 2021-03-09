
# Description:
# Theory
# Binary relation is a system which encodes relationship between elements of 2 sets of elements.
# If a pair (x, y) is present in a binary relation, it means that the element x from the first set is related to the element y from the second set.

# One of the spheres where binary relations are used is decision support systems where they define partial ordering between elements of a set.
# If a pair (x, y) is present in a binary relation, it means that the option x is better than the option y.

# Binary relation optimization is a process of searching for a set of options which are (in some way) better than other options in that binary relation.

# Task
# Given a binary relation, you have to perform an optimization on it.
# In this case, find a list of options which are collectively better than all the other options. Such options satisfy the following 2 criteria:

# all the options included in the result are not directly related to each other
# for each option not included in the result there must be at least one better option which is included in the result
# The binary relation will be provided in the form of an adjacency matrix - a matrix m where a non-zero element m[x][y]
# means that the option x is better than the option y. (You can also interpret it as an adjacency matrix of a graph,
# where the better vertex x has a unidirectional connection to the worse vertex y).

# Assume the options are numbered from 0 to n, and directly mapped to the adjacency matrix (the row m[0] specifies the relations of the option 0, the row m[1]
# specifies the relations of the option 1, and so on). Your solution should return a sorted list of options which are optimal for the given binary relation.


def find_vertices(adj):
    opt, todo = set(), {*range(len(adj))}
    while todo:
        new = {x for x in todo if not any(adj[y][x] for y in todo)}
        todo -= new
        todo -= {x for y in new for x in todo if adj[y][x]}
        opt |= new
    return sorted(opt)