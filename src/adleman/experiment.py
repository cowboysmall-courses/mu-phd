from graphs import create_vertex_strands, complement_strands, create_edge_strands, create_paths

import random


VERTS  = 7
LENGTH = 10
FACTOR = 100000

EDGES  = [
    (0, 1), (0, 3), (0, 6),
    (1, 2), (1, 3),
    (2, 1), (2, 3),
    (3, 2), (3, 4),
    (4, 1), (4, 5),
    (5, 1), (5, 2), (5, 6)
]


def main() -> None:
    print("\n")
    print("\tA Simulation of Adleman's Experiiment:")
    print("\n")

    print(f"  Original Vertices: {' -> '.join(str(i) for i in range(VERTS))}")
    print(f"     Original Edges: {', '.join(f"{i} -> {j}" for (i, j) in EDGES)}")
    print("\n")

    v_strands = create_vertex_strands(LENGTH, VERTS)
    c_strands = complement_strands(v_strands)
    e_strands = create_edge_strands(c_strands, EDGES, LENGTH)
    print(f"   Encoded Vertices: {', '.join(v_strands)}")
    print(f"        Complements: {', '.join(c_strands)}")
    print(f"      Encoded Edges: {', '.join(e_strands)}")
    print("\n")

    # Step 1: Create paths based on edges
    a_strands = v_strands * FACTOR
    random.shuffle(a_strands)
    paths = create_paths(a_strands, e_strands, v_strands[-1], LENGTH)

    # Step 2: Retain paths that begin and end with the start and end vertices
    #         (we have already checked for the exit vertices)
    paths = [path for path in paths if [path[0] == v_strands[0]]]

    # Step 3: Retain paths that contain the correct number of vertices
    paths = [path for path in paths if len(path) == VERTS]

    # Step 4: Retain paths that include all vertices
    s_strands = set(v_strands)
    paths = [path for path in paths if set(path) == s_strands]

    # Step 5: If paths exist then 'Yes' or else 'No'
    found = len(paths) > 0
    print(f"        Paths Found: {'Yes' if found else 'No'}")
    if found:
        print(f"  Paths Found Count: {len(paths)}")
        print(f" Encoded Path Found: {' -> '.join(paths[0])}")
        print(f"         Path Found: {' -> '.join([str(v_strands.index(p)) for p in paths[0]])}")
    print("\n")
